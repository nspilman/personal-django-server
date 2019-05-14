var app = new Vue({
    components:{
    },
    el: '#app',
    data: {
      name:null,
      created_user:null,
      address:null,
      startdatetime:null,
      enddatetime:null,
      },
    methods:{
        createEvent(){
          axios.defaults.xsrfCookieName = 'csrftoken';
          axios.defaults.xsrfHeaderName = 'X-CSRFToken'
          const event = {
            "name":"Patick's Party - Roooound TWO y'all!",
            "created_user":"patricksanchez",
            "startdate":"2019-06-10",
            "enddate":"2019-06-10",
            "starttime":"12:00",
            "endtime":"16:00"
          };
          console.log(event)
          axios.post(
            '/events/',
            event
          ).then(resp => console.log(resp))
        }
    },
    watch:{
      startdate(){
        console.log(this.startdate)
      }
    },
    delimiters:['${','}'],
    created(){
       this.createEvent()
    },
    computed:{
      startdate(){
      return new Date(this.startdatetime)
      },
      starttime(){

      },
      enddate(){

      },
      endtime(){

      }
    }
  })