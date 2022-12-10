import React,{useState} from 'react';
import Answer from './components/Answer';


function App() {

  const questions =[
    {
      
      answerOptions:[
        {answerText:'ドレミ',isCorrect:true},
        {answerText:'ファ',isCorrect:false},
        {answerText:'ソラシ',isCorrect:false},
        {answerText:'ド',isCorrect:false},
      ],
    },
    {
    
      answerOptions:[
        {answerText:'ドレミ',isCorrect:false},
        {answerText:'ファ',isCorrect:false},
        {answerText:'ソラシ',isCorrect:false},
        {answerText:'ド',isCorrect:true},
      ],
    },
    {
      
      answerOptions:[
        {answerText:'ドレミ',isCorrect:false},
        {answerText:'ファ',isCorrect:false},
        {answerText:'ソラシ',isCorrect:true},
        {answerText:'ド',isCorrect:false},
      ],
    },
  ];

  


  const [currentQuestion,setCurrentQuestion] = useState(0);

  const [showScore,setShowScore] = useState(false);

  const [score,setScore] = useState(0);

  const handleAnswerButtonClick = (isCorrect) => {

    if(isCorrect === true){
      
      alert('正解です');
      setScore(score+1);
    }else{
      alert('不正解です');
    }

    const nextQuestion = currentQuestion + 1;

    if(nextQuestion < questions.length){
      setCurrentQuestion(nextQuestion);
    }else{
      setShowScore(true);

    }
  }

  return (

    <div className="App">
      {
        showScore ? (
          <p>お疲れ様でした!<br></br><span class="correct">3問中{score}問</span>正解です</p>
        )
        :
        (
          <Answer
            handleAnswerButtonClick={handleAnswerButtonClick}
            questions={questions}
            currentQuestion={currentQuestion}
          />
        )
      }
    </div>
  );
}

export default App;

