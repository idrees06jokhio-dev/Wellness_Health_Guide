// Hide result box when user edits inputs again

(function(){
    var ids = ['nam'];
    function hideResult(){
      var box = document.getElementById('sresult');
      if (box) { box.style.display = 'none'; }
    }
    ids.forEach(function(id){
      var el = document.getElementById(id);
      if (!el) return;
      el.addEventListener('focus', hideResult);
      el.addEventListener('change', hideResult);
      el.addEventListener('input', hideResult);
    });
  })();