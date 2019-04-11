const loginForm =  {
    template: `
   <div>
    <input></input>
    <input></input>
   </div>
   `,
    data(){
        return{
         }
    },
}



var app = new Vue({
    components:{
        loginForm
    },
    el: '#login-form',
    data: {
      events:null,
    },
    methods:{
       async sendLogin(){
        const resp = await axios.get('/events');
        const data = await resp.data;
        this.events = await data
        }
    },
    delimiters:['${','}'],
    created(){
    }
  })

  