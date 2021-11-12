    var courses = [];
    var course_number_input = document.getElementById("code");
    var course_title_input = document.getElementById("ctitle");
    var previous_course_title = "";

    // Gets filtered autocomplete results
    function autocomplete(input)
    {
      const url = `/search_course/?course=${input}`;
      return new Promise(resolve =>
      {
        fetch(url)
        .then(response => response.json())
        .then(data => {resolve(data.data)})
      })
    }
    
    // Show filtered autocomplete. Autofills course title
    async function showResults(val)
    {
      var res = document.getElementById("result");
      if (val == '')
      {
        res.innerHTML = '';
        return;
      }
      let list = '';
      courses = await autocomplete(val);
      if (courses.length != 0)
      {
        for (i = 0; i < courses.length; i++)
        {
          list += '<li data-course-number="' + courses[i][0] + '" onmousedown="selectAutoComplete(this)">' + courses[i][1] + '</li>';
        }
        // Fills the result div with an unordered list of the autocomplete results
        res.innerHTML = '<ul>' + list + '</ul>';
        // Autofill course title if there is one
        course_title_input.value = courses[0][1];
      }
      else
      {
        res.innerHTML = '';
        // Clear course_title field if 
        course_title_input.value = previous_course_title;
      }
    }

    // Autocomplete with first suggestion
    function selectFirst()
    {
      if (courses.length != 0)
      {
        course_number_input.value = courses[0][0];
        course_title_input.value = courses[0][1];
      }
    }

    // Pressing Enter or Tab autocompletes with first suggestion
    course_number_input.addEventListener("keydown", function(event)
    {
      if (event.key == 'Enter' || event.key == 'Tab')
      {
        // Autofills only when there is input
        if (course_number_input.value != "")
        {
          selectFirst();
        }
        // Clears autocomplete results
        if (this.res)
        {
          this.res.innerHTML = '';
        }
      }
    })
    
    // Input triggers autocomplete
    course_number_input.addEventListener("input", debounce(function() 
    {showResults(course_number_input.value)}, 250));
    
    // Exiting course number input clears filtered list
    course_number_input.addEventListener("blur", function()
    {
      var res = document.getElementById("result");
      res.innerHTML = '';
    })
    
    // Remembers previous course title entered
    course_number_input.addEventListener("focus", function()
    {
      previous_course_title = course_title_input.value;
    })

    // Clicking on suggestion from list autocompletes text fields
    function selectAutoComplete(course)
    {
      course_number_input.value = course.getAttribute("data-course-number");
      course_title_input.value = course.innerText;
    }

    // Adds debouncing to a function
    function debounce(func, timeout)
    {
      let timer;
      return function(...args)
      {
        if(timer)
        {
          clearTimeout(timer);
        }
        timer = setTimeout(() => { func(this, args); }, timeout);
      };
    }