<template>
  <div id="app">
    <v-app>
      <v-container fluid>
        <v-row class="justify-center mt-2">
          <h1>List of Tasks</h1>
        </v-row>
        <v-row class="justify-center mt-2">
          <task-form @reloadData="loadTasks" />
        </v-row>

        <v-row
          v-for="(task, index) in tasks"
          :key="index"
        >
          <v-card
            class="mx-auto mt-2"
            :flat="true"
            :width="500"
            :outline="true"
            :disabled="!!task.completed_at"
          >
            <v-card-title primary-title>
              <div class="headline">{{ task.title }}</div>
            </v-card-title>
            <v-card-text>
              Description: {{ task.description }}<br>
              Deadline: {{ task.deadline }}<br>
              Completed at: {{ task.completed_at }}
            </v-card-text>
            <v-card-actions>
              <v-btn
                fluid
                text
                :disabled="!!task.completed_at"
                @click="doneTask(task.id)"
              >Done</v-btn>
            </v-card-actions>
          </v-card>
        </v-row>
      </v-container>
    </v-app>
  </div>
</template>

<script>

import TaskForm from '@/components/Tasks.vue'

export default {
  name: 'app',
  components: {
    TaskForm
  },
  data () {
    return {
      tasks: []
    }
  },
  methods: {
    async doneTask (id) {
      await this.axios.post(`/tasks/${id}/done/`)
      this.loadTasks()
    },
    loadTasks () {
      this.axios.get('/tasks/')
        .then(res => { this.tasks = res.data })
        .catch(error => {
          console.log(error)
        })
    }
  },
  mounted () {
    this.loadTasks()
  }
}
</script>