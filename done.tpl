<html>
<head>
<link href="/css/bootstrap.css" rel="stylesheet">
<title>Meeting Rollcall - Report</title>
</head>
<body>
<div class="container">
    <div class="span4">
    <a href="/"><i class="icon-home"></i></a>
    
    </div>
    <div class="span4">
        <h1>Attendance Report</h1>

        <table class="table table-bordered table-condensed">
        <thead>
        <tr>
            <th>Present</th>
            <th>Absent</th>
            <th>Percentage Present</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td>{{ present }}</td>
            <td>{{ absent }}</td>
            <td>{{ percentage }}</td>
        </tr>
        </tbody>
        </table>

<h1>Quorum Status: {{ quorum }}</h1>
    </div>
</div>
</body>
</html>
