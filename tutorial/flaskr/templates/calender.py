"""月ごとのカスタムカレンダーのhtmlを作成し、ブラウザで開く."""
import calendar
import webbrowser

BASE_HTML = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <!-- ここにカレンダーを挿入する　-->
        {}
    </div>
    <!-- jQuery first, then Tether, then Bootstrap JS. -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.0.0/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.2.0/js/tether.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js"></script>
</body>
</html>
"""


class MyCalendar(calendar.LocaleHTMLCalendar):
    """カスタムカレンダー."""

    def formatmonthname(self, theyear, themonth, withyear=True):
        """tableタグの一番上、タイトル部分にあたるhtmlを作成する."""
        return '<tr><th colspan="7" class="month">Hello World</th></tr>'

    def formatday(self, day, weekday):
        """tableタグの日付部分のhtmlを作成する<td>...</td>."""
        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        else:
            base_html = '<td class="{}"><a href="#">{}</a></td>'
            return base_html.format(self.cssclasses[weekday], day)

    def formatmonth(self, theyear=None, themonth=None, withyear=True):
        """月のカレンダーを作成する."""
        if theyear is None:
            theyear = self.date.year
        if themonth is None:
            themonth = self.date.month
        v = []
        a = v.append
        # classにtableを足しただけ！
        a('<table class="month table">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)


my_calendar = MyCalendar()
my_calendar_html = my_calendar.formatmonth(2018, 10)
result_html = BASE_HTML.format(my_calendar_html)
with open('calendar.html', 'w') as file:
    file.write(result_html)

webbrowser.open_new('calendar.html')