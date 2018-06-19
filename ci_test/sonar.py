#-*- coding:utf-8 -*-

__author__ = 'wangjf'

'''
主要指标：
代码覆盖率 coverage
单元测试成功 test_success_density
重复率 duplicated_lines_density
'''

class SonarReport:

    def __init__(self,  name):
        self._url = 'http://10.213.3.181:9000'
        self._name = name

    @staticmethod
    def get_response(url, param=None, flag=1):
        import requests
        data = None
        try:
            res = requests.get(url, params=param)
            data = res.text if flag else res.json()
            return data
        except requests.RequestException:
            print('connect fail')

    # 通过名字获取id
    def name_to_id(self,name):
        # GET 获取项目信息API
        index_url = '/api/projects/index'
        param = {'search': name}
        project_id = self.get_response(self._url + index_url, param=param, flag=0)
        return project_id[0].get('id') if project_id else 0

    # 获取sonar报告
    def get_sonar_report(self):

        sonar_id = self.name_to_id(self._name)
        if sonar_id:
            project_detail = self._url + '/dashboard/index/{}'.format(sonar_id)
            response = self.get_response(project_detail)
        return response

    # 获取指标
    def get_metrics(self, metrics):
        metric = []
        # 指标资源API
        resource = '/api/resources'
        param = {
            'resource': self.name_to_id(self._name),
            'metrics': metrics
        }
        # 找不到项目或者项目名
        if param.get('resource') == 0:
            return ''
        res = self.get_response(self._url + resource, param=param, flag=0)
        if res:
            detail = res[0].get('msr')
            metric = detail[0].get('frmt_val')
        return metric

    # 分析结果
    def analysis(self):

        duplicate_rate = self.get_metrics('duplicated_lines_density') or '0.0%'
        cover_rate = self.get_metrics('coverage') or '0.0%'
        unit_rate = self.get_metrics('test_success_density') or '0.0%'
        return [duplicate_rate, cover_rate, unit_rate]

if __name__ == '__main__':
    import sys
    #main_url = 'http://10.213.3.181:9000'
    project_name = 'pallet Maven Webapp'
    #project_name = sys.argv[0]
    sonar_report = SonarReport(project_name)
    result = sonar_report.analysis()
    print('代码重复率: {0}, 代码覆盖率: {1}, 单元测试成功率: {2}.'.format(result[0], result[1], result[2]))
