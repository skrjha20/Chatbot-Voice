var lastSentMessage = "";
var lastRecievedMessage = 1;
var ButtonClicked = false;


var DEFAULT_TIME_DELAY = 2000;
var $chatlogs = $('.chatlogs');
$( window ).load(function() {
  speechResponse("hello");
});

$('document').ready(function(){
	$(function() {
	 	$('textarea').spellAsYouType();
	});
	document.getElementById("inputTextArea").focus();
	$("#switchInputType").toggle();
	$("#switchInputType").click(function(event) {
		if($('.buttonResponse').is(":visible")) {
			$("#switchInputType").attr("src", "static/Images/multipleChoice.png");
		}
		else {
			$("#switchInputType").attr("src", "static/Images/keyboard.png");
		}
		$('textarea').toggle();
		$('.buttonResponse').toggle();
	});

	$("textarea").keypress(function(event) {
		$("#rec").attr("src", "static/Images/MicrophoneOff.png");
		document.getElementById("rec").disabled = true;
		if(event.which === 13) {
			event.preventDefault();
			ButtonClicked = false;
			send(this.value);
			$("#rec").attr("src", "static/Images/microphone.png");
			document.getElementById("rec").disabled = false;
			$(".input").attr("rows", "1");
			this.value = "";
			if($("#switchInputType").is(":visible")) {
				$("#switchInputType").toggle();
				$('.buttonResponse').remove();
			}
		}
	});
	
	$("#rec").click(function(event) {
		switchRecognition();
	});

	$('.chat-form').on("click", '.buttonResponse', function() {
		ButtonClicked = true;
		send(this.innerText);
		$('textarea').toggle();
		$('.buttonResponse').toggle();
		$('#switchInputType').hide();
		$('.buttonResponse').remove();
	});
})

function send(text) {
	$chatlogs.append(
        $('<div/>', {'class': 'chat self'}).append(
        	$('<p/>', {'class': 'chat-message', 'text': text}),
        	$('<div/>', {'class': 'user-photo'}).append($('<img src="static/Images/ana.JPG" />'))
            ));
			
	var $sentMessage = $(".chatlogs .chat").last();
	checkVisibility($sentMessage);
	lastSentMessage = text;

	$.ajax({
		type: "POST",
		url: "/ask",
		contentType: "application/json; charset=utf-8",
		dataType: "json",
		data: JSON.stringify({query: text}),
		success: function(data) {
            console.log(data);
			if(data.type == 'img'){
				showLoading();
				newRecievedMessage(JSON.stringify(data.answer));
				speechResponse(JSON.stringify(data.answer));
				newRecievedImages(data.images);
			}
            else {
				newRecievedMessage(JSON.stringify(data.answer));
				speechResponse(JSON.stringify(data.answer_word));
			}
		},
		error: function() {
			newRecievedMessage("Sorry, I don't have answer to this query");
		}
	});
}


function newRecievedImages(imgs) {
	showLoading();
	setTimeout(function () {
		createNewImages(imgs);
	},DEFAULT_TIME_DELAY);
}

function createNewImages(imgs) {
	date = new Date();
	gallery_id = date.getTime().toString();
	hideLoading();
	$chatlogs.append(
		$('<div/>', {'class': 'chat friend'}).append(
			$('<div/>', {'class': 'user-photo'}).append($('<img src="static/Images/ana.JPG" />')),
			$('<a/>',{'class': 'chat-message', 'href': imgs[0], 'target': '_blank', 'text':imgs[0]}),
			$('<div/>', {'id': gallery_id})));

	var $newMessage = $(".chatlogs .chat").last();
	checkVisibility($newMessage);
	hideLoading();
	$('#' + gallery_id).imagesGrid({images: imgs});
}


function newRecievedMessage(messageText) {
	var removedQuotes = messageText.replace(/[""]/g,"");
	lastRecievedMessage = removedQuotes;
	if(removedQuotes.includes("<ar"))
	{
		buttonResponse(removedQuotes);	
	}
	else if (removedQuotes.includes("<br")) 
	{
		multiMessage(removedQuotes);
	}
	else
	{
		showLoading();
		setTimeout(function() {
			createNewMessage(removedQuotes);
		}, DEFAULT_TIME_DELAY);
	}
}

function multiMessage(message)
{
	var matches;
	var listOfMessages = [];
	var regex = /\<br(?:\s+?(\d+))?\>(.*?)(?=(?:\<br(?:\s+\d+)?\>)|$)/g;
	while(matches = regex.exec(message))
	{
		if(matches[1] == undefined)
		{
			matches[1] = DEFAULT_TIME_DELAY;
		}
		var messageText  = matches[2].split(/<ar>/);
		listOfMessages.push({
				text: messageText[0],
				delay: matches[1]
		});
	}
	var i = 0;
	var numMessages = listOfMessages.length;
	showLoading();
	(function theLoop (listOfMessages, i, numMessages) 
	{
		setTimeout(function () 
		{
			createNewMessage(listOfMessages[i].text);
			if (i++ < numMessages - 1) 
			{
				showLoading();
				theLoop(listOfMessages, i, numMessages);
			}
		}, listOfMessages[i].delay);
	})(listOfMessages, i, numMessages);
}

function buttonResponse(message)
{
	var matches;
	var $input;
	multiMessage(message);
	var regex = /\<br(?:\s+?(\d+))?\>(.*?)(?=(?:\<ar(?:\s+\d+)?\>)|$)/g;
	matches = regex.exec(message);
	console.log(matches);
	var buttonList = message.split(/<ar>/);
	buttonList = buttonList.splice(1);
	console.log(buttonList);
	var listOfInputs = [];
	for (var index = 0; index < buttonList.length; index++)
	{
		var response = buttonList[index];
		$input = $('<div/>', {'class': 'buttonResponse' }).append(
            $('<p/>', {'class': 'chat-message', 'text': response}));
		listOfInputs.push($input);
	}
	
	showLoading();
	setTimeout(function() {
		$('textarea').toggle();
		$("#switchInputType").show();
		for (var index = 0; index < listOfInputs.length; index++) {
			listOfInputs[index].appendTo($('#buttonDiv'));
		}
	}, matches[1]);
}

function createNewMessage(message) {
	hideLoading();
	//speechResponse(message);
	$chatlogs.append(
		$('<div/>', {'class': 'chat friend'}).append(
			$('<div/>', {'class': 'user-photo'}).append($('<img src="static/Images/ana.JPG" />')),
			$('<p/>', {'class': 'chat-message', 'text': message})));
	var $newMessage = $(".chatlogs .chat").last();
	checkVisibility($newMessage);
}

function showLoading()
{
	$chatlogs.append($('#loadingGif'));
	$("#loadingGif").show();
	$('.chat-form').css('visibility', 'hidden');
 }

function hideLoading()
{
	$('.chat-form').css('visibility', 'visible');
	$("#loadingGif").hide();
	$(".input").val("");
	$(".input").attr("rows", "1");
	$(".input").focus();
}

function checkVisibility(message)
{
	$chatlogs.stop().animate({scrollTop: $chatlogs[0].scrollHeight});
}

var recognition;
function startRecognition() {
	document.getElementById("inputTextArea").disabled = true;
    console.log("Start")
	recognition = new webkitSpeechRecognition();
	recognition.onstart = function(event) {
        console.log("Update");
		updateRec();
	};
	
	recognition.onresult = function(event) {	
		var text = "";	
		for (var i = event.resultIndex; i < event.results.length; ++i) {
			text += event.results[i][0].transcript;
		}	
		setInput(text);
		stopRecognition();	
	};	
	recognition.onend = function() {
		stopRecognition();
	};	
	recognition.lang = "en-US";
	recognition.start();
}

function stopRecognition() {
	if (recognition) {
        console.log("Stop Recog");
		recognition.stop();
		recognition = null;
	}
	updateRec();
}

function switchRecognition() {
	if (recognition) {
        console.log(" Stop if");
		stopRecognition();
	} else {
		startRecognition();
	}
}

function setInput(text) {
	$(".input").val(text);	
    send(text);
	document.getElementById("inputTextArea").disabled = false;
	document.getElementById("inputTextArea").focus();
    $(".input").val("");    
}

function updateRec() {
	if (recognition) {
		$("#rec").attr("src", "static/Images/MicrophoneOff.png");
	} else {
		$("#rec").attr("src", "static/Images/microphone.png");
	}
}

function speechResponse(message)
{
	var msg = new SpeechSynthesisUtterance();
	msg.default = false;
 	msg.voiceURI = "Fiona";
	msg.name = "Fiona";
	msg.localService = true;
  	msg.text = message;
  	msg.lang = "en";
	msg.rate = .9;
	msg.volume = 1;
	msg.voice = speechSynthesis.getVoices().filter(function(voice) {
	return voice.name == "Microsoft Zira Desktop - English (United States)";
    })[0];
  	window.speechSynthesis.speak(msg);
}

$(document)
    .one('focus.input', 'textarea.input', function(){
        var savedValue = this.value;
        this.value = '';
        this.baseScrollHeight = this.scrollHeight;
        this.value = savedValue;
    })
    .on('input.input', 'textarea.input', function(){
        var minRows = this.getAttribute('data-min-rows')|0, rows;
        this.rows = minRows;
        rows = Math.ceil((this.scrollHeight - this.baseScrollHeight) / 17);
        this.rows = minRows + rows;
	});
	