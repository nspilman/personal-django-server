console.log('you found me! Woohoo!')

const event =  {
    template: `
    <div class = "eventCard card p-4">
    <div class = "row">
        <div class = "col-sm-3">
        <a :href="eventLink">
        <img :src="imageUrl"/>
        </a>
        </div>
        <div class = "col-sm-9">
          <h1> {{event.name}}</h1>
          <h4>{{date}}</h4>
          <h6 v-if="attendees">attendees: {{attendees.length}}</h6>
          <h6 >Host:<a :href="'/frontend/person/'+event.created_user"> {{event.created_user}}</a></h6>
          </div>
          </div>
    </div>`,
    data(){
        return{
            attendees:null,
            imageUrl:"https://source.unsplash.com/300x200/?event/" + this.event.name,
            eventLink: "/frontend/event/" + this.event.id
        }
    },
    computed:{
        date(){
            const {startdate, enddate} = this.event
            if(startdate === enddate){
                let date = startdate;
                return new Date(date).toDateString()  
            } 
        }
    },
        methods:{
            async getAttendees(){
              const resp = await axios.get(`/events/eventsignups/${this.event.id}`)
              const data = await resp.data
              this.attendees = data.attendees
            }
        },
        created(){
          this.getAttendees()  
        },
    props:['event'],
    }

var app = new Vue({
    components:{
        event
    },
    el: '#app',
    data: {
      events:null,
    },
    methods:{
       async getEvents(){
        const resp = await axios.get('/events');
        const data = await resp.data;
        this.events = await data
        console.log(this.events)
        }
    },
    delimiters:['${','}'],
    created(){
       this.getEvents()
    }
  })

  