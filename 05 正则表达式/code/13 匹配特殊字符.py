

html = """
<script type="text/javascript">
    var fp = new FlexPaperViewer(
        'http://bulletin.sntba.com/FlexPaperViewer',
        'viewerPlaceHolder', {
            config : {
                SwfFile : escape('http://bulletin.sntba.com/project//2020-01/noticeFile/Z6101002181N01555001/8aa946a756a24b09aded43c7bdd5f348.swf'),
                EncodeURI : true,
                Scale : 0.6,
                ZoomTransition : 'easeOut',
                ZoomTime : 0.5,
                ZoomInterval : 0.05,
                FitPageOnLoad : true,
                FitWidthOnLoad : true,
                PrintEnabled: false,//是否支持打印
                FullScreenAsMaxWindow : false,
                ProgressiveLoading : true,
                MinZoomSize : 0.05,
                MaxZoomSize : 5,
                SearchMatchAll : false,
                InitViewMode : 'Portrait',
                ViewModeToolsVisible : true,
                ZoomToolsVisible : true,
                NavToolsVisible : true,
                CursorToolsVisible : true,
                SearchToolsVisible : false,
                localeChain : 'zh_CN'
            }
        });
</script>
"""
'''
上面的html字符串用到了三引号！
'''
import re

# 一旦字符串中有元字符作为约束, 那么需要用转义字符'\'转译成普通字符串
result = re.findall("SwfFile : escape\('(.*?)'\),", html, re.S)
print(result)

# 不要在正则中用原生字符串
result = re.findall(r"SwfFile : escape('(.*?)'),", html, re.S)
print(result)

# (.*?)
