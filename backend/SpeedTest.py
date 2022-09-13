import cProfile
import MyFunction
import pstats

cProfile.run('MyFunction.getPageInfo(\'http://www.nhc.gov.cn/xcs/yqtb/202209/8ac84d72227c4a318694ddae45412c9a.shtml\')','restats')

p = pstats.Stats('restats')
p.sort_stats('cumulative').print_stats(10)