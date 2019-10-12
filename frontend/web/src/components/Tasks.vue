<template>
  <v-container class="text-center">
    <v-snackbar v-model="snackbar">
      Task successfull saved!
    </v-snackbar>
    <v-dialog
      v-model="dialog"
      persistent
    >
      <template v-slot:activator="{ on }">
        <v-btn
          inline
          v-on="on"
        >New Task</v-btn>
      </template>

      <v-card>
        <v-card-title primary-title>
          New Task
        </v-card-title>
        <v-card-text>
          <v-form v-model="formValid">
            Deadline:
            <Datepicker
              format="YYYY-MM-DD"
              width="50%"
              heigth="50%"
              label="Date"
              v-model="form.deadline"
            /><br>
            <v-text-field
              label="Title"
              v-model="form.title"
              :rules="[v => !!v || 'Title is required']"
            /><br>
            <v-textarea
              label="Description"
              v-model="form.description"
              :rules="[v => !!v || 'Description is required']"
            />
          </v-form>
        </v-card-text>

        <v-card-actions>
          <v-btn
            color="red"
            text
            @click="dialog = false"
          >
            Cancel
          </v-btn>
          <v-spacer />
          <v-btn
            color="green"
            text
            @click="saveTask"
            :disabled="!formValid"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>

    </v-dialog>
  </v-container>
</template>

<script>
import Datepicker from 'vuejs-datetimepicker'
export default {
  watch: {
    dialog (value) {
      if (!value) {
        this.$emit('reloadData')
      }
    }
  },
  components: {
    Datepicker
  },
  data () {
    return {
      dialog: false,
      snackbar: false,
      form: {},
      formValid: false
    }
  },
  methods: {
    async saveTask () {
      const res = await this.axios.post('/tasks/', this.form)
      if (res.status === 201) {
        this.form = {}
        this.dialog = false
        this.snackbar = true
      }
    }
  }
}
</script>