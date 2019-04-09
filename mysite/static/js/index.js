console.log('you found me! Woohoo!')

const event =  {
    template: `
    <div class = "container eventCard card p-3">
          <h1> {{event.name}}</h1>
          <h4>{{date}}</h4>
    </div>`,
    data(){
        return{
        }
    },
    computed:{
        date(){
            const {startdate, enddate} = this.event
            console.log(startdate === enddate)
            if(startdate === enddate){
                let date = startdate;
                return new Date(date).toDateString()  
            } 
        }
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
        this.events = data
        console.log(data) 
        }
    },
    delimiters:['${','}'],
    created(){
       this.getEvents()
    }
  })

  