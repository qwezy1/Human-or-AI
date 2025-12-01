<script setup>
import { ref } from "vue";

const text = ref("");
const result = ref(null);
const loading = ref(false);
const error = ref(null);

async function sendRequest() {
  loading.value = true;
  error.value = null;
  result.value = null;

  try {
    const res = await fetch("http://localhost:3000/api/main", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: text.value }),
    });

    if (!res.ok) throw new Error("Ошибка запроса");

    result.value = await res.json();
  } catch (e) {
    error.value = e.message;
  } finally {
    loading.value = false;
  }
}
</script>

<template>
  <div style="max-width: 600px; margin: 40px auto; font-family: sans-serif;">
    <h2>News AI Detector — Frontend</h2>

    <textarea
      v-model="text"
      placeholder="Введите текст..."
      style="width:100%; height:150px; margin-bottom:10px;"
    ></textarea>

    <button @click="sendRequest" :disabled="loading">
      {{ loading ? "Загрузка..." : "Отправить" }}
    </button>

    <div v-if="result" style="margin-top:20px;">
      <h3>Ответ сервера:</h3>
      <pre>{{ result }}</pre>
    </div>

    <div v-if="error" style="color:red; margin-top: 20px;">
      Ошибка: {{ error }}
    </div>
  </div>
</template>

<style>
button {
  padding: 10px 20px;
  cursor: pointer;
}
</style>
