console.log('you found me! Woohoo!')

const event =  {
    template: `
    <div class = "eventCard col-sm-4 card p-4">
        <a :href="eventLink">
            <div class = 'text-center'>
                <img :src="imageUrl" class = "p-3"/>
            </div>
        </a>
        <div class = "px-5">
            <h4> 
                {{event.name}}
            </h4>
            <h6>
                {{date}}
            </h6>
            <h6 v-if="attendees">
                attendees: {{attendees.length}}
            </h6>
            <h6 >
                Host:
                <a :href="'/frontend/person/'+event.created_user"> 
                    {{event.created_user}}
                </a>
            </h6>
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
        }
    },
    delimiters:['${','}'],
    created(){
       this.getEvents()
    }
  })

  