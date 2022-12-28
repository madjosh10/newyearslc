let calendarEl = document.getElementById('calendar');
let calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'listWeek',
    aspectRatio: 2,
    events : [
        {% for event in events %}
        {
            title : '{{event.title}}',
            start : '{{event.start}}',
            end : '{{event.end}}',
            
        },
        {% endfor %}
    ]
});
calendar.render();