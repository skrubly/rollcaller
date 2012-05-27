<html>
<head>
<link href="/css/bootstrap.css" rel="stylesheet">
<title>Meeting Rollcall</title>
</head>
<body>
<div class="container" style="padding-top:20px;">



<h1 align="center" style="font-size: 70;line-height:110%;">{{ meeting['name'] }}</h1>
<h2 align="center" style="padding-top:20px">Group Number: {{ meeting['number'] }}</h1>
<h3 align="center">Day: {{ meeting['day'] }}</h3>

% if meeting['present'] == 0:
%    presentstr = "Absent"
%  elif meeting['present'] == 1:
%    presentstr = "Present"
% end

<h4 align="center" style="font-size:40;padding-top:20px;"><a href="/present/{{ meeting['id'] }}">{{ presentstr }}</a></h4>

<h4 align="center" style="padding:20px;">Notes: {{ meeting['notes'] }}</td>
<form method="POST">
<input name="notes" type="text" />
<input type="submit" value="Submit">
</form>

<a href="/show/{{ prevlink }}">Prev</a> <a href="/"><i class="icon-home"></i></a> <a href="/show/{{ nextlink }}">Next</a>
</div>
</body>
</html>
