var app = new Vue({
    components:{
    },
    el: '#login-form',
    data: {
      events:null,
      username:null,
      password:null,
      loggedIn:false,
    },
    methods:{
       async sendLogin(){
        const resp = await axios.get('/events');
        const data = await resp.data;
        this.events = await data
        },
        async postLogin(){
            axios.post(
                '/events/login/',
                {
                    username:this.username,
                    password:this.password
                }
            ).then(resp => console.log(resp))
        }
    },
    delimiters:['${','}'],
    created(){
    },
  })

  