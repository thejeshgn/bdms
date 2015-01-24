window.fbAsyncInit = function() {
  FB.init({
    appId: '1502592940005228',
    cookie: true,
    xfbml: true,
    oauth: true
  });
  
  FB.Event.subscribe('auth.login', function(response) {
    window.location.reload();
  });
  
  FB.Event.subscribe('auth.logout', function(response) {
    //window.location.reload();
  });
};


(function() {
  var e = document.createElement('script'); e.async = true;
  e.src = document.location.protocol +
    '//connect.facebook.net/en_US/all.js';
  document.getElementById('fb-root').appendChild(e);
  
}());

function setCookie(cname,cvalue,minutes) {
  var d = new Date();
  d.setTime(d.getTime() + (minutes*60*1000));
  var expires = "expires=" + d.toGMTString();
  document.cookie = cname+"="+cvalue+"; "+expires;
}

function getCookie(cname) {
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i=0; i<ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0)==' ') c = c.substring(1);
    if (c.indexOf(name) != -1) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

location_detected = getCookie("location");
if (location_detected=='') {
  recordPosition(1);
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(recordPosition, recordPosition);
  } else {
    recordPosition(0);
  }
}

function recordPosition(position) {
  update = 0;
  lat = 0;
  lng = 0;
  if (position.code==1 && position != 1) {
    setCookie("location", 'recorded', 1440);
  } else if (position!=1) {
    lat = position.coords.latitude;
    lng = position.coords.longitude;
    update = 1
    setCookie("location", 'recorded', 1440);
  }
  setCookie("location_lat", lat, 1440);
  setCookie("location_lng", lng, 1440);
  $.ajax({
    type: 'POST',
    url: '/vb/savevisitor/',
    crossDomain : true,
    data : { lat : lat, lng : lng, update:update },
    success: function(response) {
      if (response) {
        console.log(response);
      }
    }
  });
}

