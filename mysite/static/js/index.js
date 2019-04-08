console.log('you found me! Woohoo!')

const event =  {
    template: `
    <div>
        <li>
            {{event.name}}
        </li>
    </div>`,
    data(){
        return{
        }
    },
    props:['event']
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

  