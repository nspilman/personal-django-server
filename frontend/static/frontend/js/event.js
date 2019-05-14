var app = new Vue({
    components:{
    },
    el: '#app',
    data: {
      event:null,
      attendees:null,
      imgUrl: "https://source.unsplash.com/1600x900/?events/" + event
      
    },
    methods:{
       async getEvents(){
        const resp = await axios.get(`/events/eventsignups/${event}`);
        const data = await resp.data;
        const {event_info, attendees} = await data
        this.attendees = await attendees
        this.event = await event_info
        console.log(this.event)
        },
    },
    delimiters:['${','}'],
    created(){
      this.getEvents()
    },
    computed:{
    }
  })