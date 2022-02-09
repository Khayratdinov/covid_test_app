
  const timeElement = document.getElementById('time');
  const resultElement = document.getElementById('result');
  const targetTime = new Date(timeElement.textContent);

  let interval = setInterval(tick, 1000);
  tick()

  function complete() {
      if (interval != null) {
          clearInterval(interval);
      }
      timeElement.textContent = 'Expired certificate';
      timeElement.classList.add('expired');
      resultElement.classList.add('expired');
      console.log("complete");
  }

  function tick(){
      const t = targetTime.getTime() - Date.now();

      if (t <= 0){
          complete();
          return;
      }

      updateTime(t);
  }

  function toFormat(n){
      return n < 10 ? '0' + n : n;
  }

  function updateTime(t){
      const d = Math.floor(t / (1000 * 60 * 60 * 24));
      const h = Math.floor((t % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const m = Math.floor(t / 1000 / 60 % 60);
      const s = Math.floor(t / 1000 % 60);

      timeElement.innerHTML = `${toFormat(d)} day ${toFormat(h)} h: ${toFormat(m)} m: ${toFormat(s)} s`;
  }
