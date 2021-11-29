<template>
  <div class="container mt-5">
    <section>
      <div class="row">
        <div class="col-8">
          <h3>Add New Mental Health Entry</h3><hr/>

          <form @submit.prevent="submit">
            <div class="mb-3">
              <label for="title" class="form-label">Title:</label>
              <input type="text" name="title" v-model="form.title" class="form-control" />
            </div>
            <div class="mb-3">
              <label for="notes" class="form-label">Notes:</label>
              <textarea
                name="notes"
                v-model="form.notes"
                class="form-control"
              ></textarea>
            </div>
            <div class="mb-3">
              <label for="content" class="form-label">Rating (1-5):</label>
              <select name="rating" v-model="form.rating" class="form-control">
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
          </form>
        </div>
        <div class="col-4">
           <h3>Tips</h3><hr/>

        </div>
      </div>
    </section>
    <section class="mt-3">
      <div class="row">
        <div class="col-12">
          <h3>Previous Entries</h3>
          <hr/>
            <div v-if="mhs.length" class="row">
              <div v-for="mh in mhs" :key="mh.id" class="notes col-3">
                <div class="card" style="width: 18rem;">
                  <div class="card-body">
                      <strong>Title:</strong> {{ mh.title }} <br/>
                      <strong>Notes:</strong> {{ mh.notes }} <br/>
                      <strong>rating:</strong> {{ mh.rating }} <br/>
                      <strong>Created at:</strong> {{ formatDate(mh.created_at)}}
                  </div>
                </div>
              </div>
            </div>

            <div v-else class="row">
              <p>Nothing to see. Check back later.</p>
            </div>
          
        </div>
      </div>
    </section>

    
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import moment from 'moment'

export default {
  name: 'Dashboard',
  components: {
     
  },
  data() {
    return {
      mhtips: [],
      form: {
        title: '',
        notes: '',
      },
    };
  },
  created: function() {
    return this.$store.dispatch('getMhs');
  },
  computed: {
    ...mapGetters({ mhs: 'stateMhs'}),
    
  },
  methods: {
    ...mapActions(['createMh']),
    async submit() {
      await this.createMh(this.form);
    },
    formatDate(value){
       return moment(String(value)).format('MM/DD/YYYY hh:mm')
    }
  },
};
</script>