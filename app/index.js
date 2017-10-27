// Require moment.js
const moment = require('moment');
// Require ipcRender
const {ipcRenderer} = require('electron');


// Listen to the 'timer-change' event
ipcRenderer.on('timer-change', (event, t) => {
  // Initialize time with value send with event
  let timeleft = t;

  // Execute every second
  let timer = setInterval(() => {


    // setup the time and subtract a second
    timeleft = moment.duration(timeleft, "minutes").subtract(1, "seconds");

    // if timer has finished display notification
    if (timeleft == 0) {
      let myNotification = new Notification('Tymer', {
        body: "Timer's Done"
      })
    }

    formattedTime = moment(timeleft.asMilliseconds()).format('mm:ss');

    // Print out the time
    timerDiv.innerHTML = formattedTime;

    // When reaching 0. Stop.
    if (timeleft <= 0) {
      clearInterval(timer);
    }
  }, 1000); // 1 second
});


