<script setup>
import { ref, reactive, onMounted } from "vue";

// Ввод текста пользователем
const text = ref("");
// Результат API
const result = reactive({
  prediction: "",
  confidence: 0,
  visible: false
});
// Состояние загрузки
const loading = ref(false);
const error = ref(null);
// История результатов
const history = ref([]);

// Функция отправки запроса
async function sendRequest() {
  if (!text.value) return;

  loading.value = true;
  error.value = null;
  result.visible = false;

  try {
    const res = await fetch("http://localhost:3000/api/main", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: text.value }),
    });

    if (!res.ok) throw new Error("Ошибка запроса");

    const data = await res.json();
    result.prediction = data.prediction;
    result.confidence = data.confidence;
    result.visible = true;

    // Добавляем в историю
    history.value.unshift({
      text: text.value,
      prediction: data.prediction,
      confidence: data.confidence
    });

    text.value = "";
  } catch (e) {
    error.value = e.message;
  } finally {
    loading.value = false;
  }
}

// Фоновая анимация частиц
const particles = ref([]);
onMounted(() => {
  for (let i = 0; i < 30; i++) {
    particles.value.push({
      x: Math.random() * 100,
      y: Math.random() * 100,
      size: Math.random() * 10 + 5,
      speedX: (Math.random() - 0.5) * 0.2,
      speedY: (Math.random() - 0.5) * 0.2,
      rotate: Math.random() * 360
    });
  }
  animateParticles();
});

function animateParticles() {
  particles.value.forEach(p => {
    p.x += p.speedX;
    p.y += p.speedY;
    if (p.x < 0) p.x = 100;
    if (p.x > 100) p.x = 0;
    if (p.y < 0) p.y = 100;
    if (p.y > 100) p.y = 0;
    p.rotate += 0.5;
  });
  requestAnimationFrame(animateParticles);
}
</script>

<template>
  <div class="app-container">
    <!-- Фоновые частицы -->
    <div class="particles">
      <div
        v-for="(p, index) in particles"
        :key="index"
        class="particle"
        :style="{
          left: p.x + '%',
          top: p.y + '%',
          width: p.size + 'px',
          height: p.size + 'px',
          transform: 'rotate(' + p.rotate + 'deg)'
        }"
      ></div>
    </div>

    <!-- Hero -->
    <header class="hero">
      <h1 class="title">News AI Detector</h1>
      <p class="subtitle">Определи, кто написал новость — человек или искусственный интеллект</p>
      <button @click="document.querySelector('.input-section').scrollIntoView({ behavior: 'smooth' })" class="btn-hero">
        Начать проверку
      </button>
    </header>

    <!-- Input Section -->
    <section class="input-section">
      <textarea
        v-model="text"
        placeholder="Вставьте текст новости здесь..."
        rows="6"
        class="text-input"
      ></textarea>
      <button :disabled="loading || !text" @click="sendRequest" class="btn">
        {{ loading ? "Анализируем..." : "Определить" }}
      </button>

      <div v-if="result.visible" class="result">
        <p class="prediction">
          Результат:
          <span :class="result.prediction === 'Human-written' ? 'human' : 'ai'">
            {{ result.prediction }}
          </span>
        </p>
        <p class="confidence">Уверенность: {{ (result.confidence * 100).toFixed(1) }}%</p>
        <div class="progress-bar">
          <div
            class="progress"
            :class="result.prediction === 'Human-written' ? 'human' : 'ai'"
            :style="{ width: (result.confidence * 100) + '%' }"
          ></div>
        </div>
      </div>

      <div v-if="error" class="error">Ошибка: {{ error }}</div>
    </section>

    <!-- History Section -->
    <section class="history">
      <h2>История проверок</h2>
      <div class="history-cards">
        <div v-for="(item, index) in history" :key="index" class="card">
          <p class="text">{{ item.text }}</p>
          <p class="prediction">
            Результат:
            <span :class="item.prediction === 'Human-written' ? 'human' : 'ai'">
              {{ item.prediction }}
            </span>
            ({{ (item.confidence * 100).toFixed(1) }}%)
          </p>
        </div>
      </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
      <p> *** </p>
    </footer>
  </div>
</template>

<style>
/* Основной фон и центровка */
.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: 'Arial', sans-serif;
  color: white;
  position: relative;
  overflow: hidden;
  background: linear-gradient(135deg, #1e1e3f, #4b1e6d);
}

/* Фоновые частицы */
.particles {
  position: absolute;
  width: 100%;
  height: 100%;
  overflow: hidden;
  top: 0;
  left: 0;
  z-index: 0;
}
.particle {
  position: absolute;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  will-change: transform;
  pointer-events: none;
  animation: pulse 2s infinite alternate;
}
@keyframes pulse {
  from { opacity: 0.2; transform: scale(0.5) rotate(0deg); }
  to { opacity: 0.8; transform: scale(1.2) rotate(360deg); }
}

/* Hero */
.hero {
  text-align: center;
  padding: 6rem 2rem 3rem;
  position: relative;
  z-index: 1;
}
.title {
  font-size: 3rem;
  font-weight: bold;
  animation: fadeInDown 1s ease-out;
}
.subtitle {
  font-size: 1.5rem;
  margin-bottom: 2rem;
  animation: fadeIn 1.5s ease-out;
}
.btn-hero {
  padding: 1rem 2rem;
  font-size: 1.2rem;
  background: #8c3fff;
  border: none;
  border-radius: 1rem;
  cursor: pointer;
  transition: all 0.3s;
}
.btn-hero:hover {
  transform: scale(1.05);
  background: #b25fff;
}

/* Input Section */
.input-section {
  width: 90%;
  max-width: 700px;
  background: rgba(255, 255, 255, 0.1);
  padding: 2rem;
  border-radius: 2rem;
  box-shadow: 0 0 20px rgba(0,0,0,0.5);
  margin-bottom: 4rem;
  position: relative;
  z-index: 1;
  animation: fadeInUp 1s ease-out;
}
.text-input {
  width: 100%;
  padding: 1rem;
  border-radius: 1rem;
  border: none;
  font-size: 1.2rem;
  margin-bottom: 1rem;
  resize: none;
  transition: all 0.3s;
}
.text-input:focus {
  outline: none;
  transform: scale(1.02);
  box-shadow: 0 0 10px rgba(255,255,255,0.5);
}
.btn {
  padding: 0.8rem 2rem;
  background-color: #8c3fff;
  border: none;
  border-radius: 1rem;
  font-size: 1.2rem;
  cursor: pointer;
  transition: all 0.3s;
}
.btn:hover {
  transform: scale(1.05);
  background-color: #b25fff;
}
.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Result */
.result {
  margin-top: 2rem;
  text-align: center;
}
.prediction {
  font-size: 1.8rem;
  font-weight: bold;
}
.prediction .human { color: #4cd137; }
.prediction .ai { color: #e84118; }
.confidence { margin-top: 0.5rem; font-size: 1.2rem; opacity: 0.9; }
.progress-bar {
  margin-top: 1rem;
  width: 100%;
  height: 1rem;
  background: rgba(255,255,255,0.2);
  border-radius: 0.5rem;
  overflow: hidden;
}
.progress {
  height: 100%;
  border-radius: 0.5rem;
  transition: width 1s ease;
}
.progress.human { background-color: #4cd137; }
.progress.ai { background-color: #e84118; }
.error { margin-top: 1rem; color: #ff6b6b; font-weight: bold; }

/* History Section */
.history { width: 90%; max-width: 900px; margin-bottom: 4rem; position: relative; z-index: 1; }
.history h2 { font-size: 2rem; margin-bottom: 1rem; text-align: center; }
.history-cards { display: flex; flex-direction: column; gap: 1rem; }
.card { background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 1rem; animation: fadeInUp 0.5s ease; }
.card .text { font-size: 1rem; margin-bottom: 0.5rem; }
.card .prediction .human { color: #4cd137; font-weight: bold; }
.card .prediction .ai { color: #e84118; font-weight: bold; }

/* Footer */
.footer { padding: 2rem; text-align: center; font-size: 1rem; opacity: 0.8; position: relative; z-index: 1; }

/* Анимации */
@keyframes fadeInDown { from { opacity: 0; transform: translateY(-30px);} to { opacity: 1; transform: translateY(0);} }
@keyframes fadeInUp { from { opacity: 0; transform: translateY(20px);} to { opacity: 1; transform: translateY(0);} }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
</style>
