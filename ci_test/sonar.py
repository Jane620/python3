#-*- coding:utf-8 -*-

__author__ = 'wangjf'

'''
主要指标：
代码覆盖率 coverage
单元测试成功 test_success_density
重复率 duplicated_lines_density
'''

class SonarReport:

    def __init__(self, url, name):
        self._url = url
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
    def name_to_id(self):
        # GET 获取项目信息API
        index_url = '/api/projects/index'
        param = {'search': self._name}
        project_id = self.get_response(self._url + index_url, param=param, flag=0)
        return project_id[0].get('id') if project_id else 0

    # 获取sonar报告
    def get_sonar_report(self):
        # GET api/projects/index
        # 查询项目id
        search_project_url = self._url + '/api/projects/index'
        param = {'search': self._name}
        sonar_id = self.get_response(search_project_url, param=param, flag=0)[0].get('id')
        if sonar_id:
            project_detail = self._url + '/dashboard/index/{}'.format(sonar_id)
            response = self.get_response(project_detail)
        return response

    # 获取指标
    def get_metrics(self, metrics):
        metric = []
        # GET 指标资源API
        resource = '/api/resources'
        param = {
            'resource': self.name_to_id(),
            'metrics': metrics
        }
        res = self.get_response(self._url + resource, param=param, flag=0)
        if res:
            detail = res[0].get('msr')
            metric = detail[0].get('frmt_val')
        return metric

    # 分析结果
    def analysis(self):

        cover_rate = self.get_metrics('coverage') or '0.0%'
        unit_rate = self.get_metrics('test_success_density') or '0.0%'
        duplicate_rate = self.get_metrics('duplicated_lines_density') or ['0.0%']
        return [cover_rate, unit_rate, duplicate_rate]


if __name__ == '__main__':
    import sys

    main_url = sys.argv[1] or ''
    project_name = sys.argv[2] or ''
    sonar_report = SonarReport(main_url, project_name)
    result = sonar_report.analysis()
    print('代码覆盖率:{0},单元测试成功率:{1},代码重复率:{2}'.format(result[0], result[1], result[2]))
