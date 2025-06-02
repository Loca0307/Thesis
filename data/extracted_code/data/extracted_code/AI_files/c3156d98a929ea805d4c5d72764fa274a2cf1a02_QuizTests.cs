using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using QuickQuiz.QuestionLogic.Model;
using QuickQuiz.QuizLogic.Exceptions;
using QuickQuiz.QuizLogic.Model;

namespace QuickQuiz.Tests
{
    [TestClass]
    public class QuizTests
    {
        [TestMethod]
        public void CreateQuiz_ShouldInitializeQuizWithPlayerName()
        {
            // Arrange
            string playerName = "Test Player";
            var questions = new List<Question>
            {
                new Question("Question 1"),
                new Question("Question 2")
            };

            // Act
            Quiz quiz = Quiz.Create(playerName, questions);

            // Assert
            Assert.AreEqual(playerName, quiz.PlayerName);
            Assert.IsNotNull(quiz.QuizId);
            Assert.IsTrue(quiz.QuestionListReadOnly.Any());
        }

        [TestMethod]
        public void GetNextQuestion_ShouldReturnNextUnansweredQuestion()
        {
            // Arrange
            string playerName = "Test Player";
            var questions = new List<Question>
            {
                new Question("Question 1"),
                new Question("Question 2")
            };
            Quiz quiz = Quiz.Create(playerName, questions);

            // Act
            QuizQuestion nextQuestion = quiz.GetNextQuestion();

            // Assert
            Assert.IsNotNull(nextQuestion);
            Assert.AreEqual("Question 1", nextQuestion.OriginalQuestion.Text);
        }

        [TestMethod]
        [ExpectedException(typeof(ActiveQuestionNotAnsweredException))]
        public void GetNextQuestion_ShouldThrowExceptionIfActiveQuestionNotAnswered()
        {
            // Arrange
            string playerName = "Test Player";
            var questions = new List<Question>
            {
                new Question("Question 1"),
                new Question("Question 2")
            };
            Quiz quiz = Quiz.Create(playerName, questions);
            QuizQuestion nextQuestion = quiz.GetNextQuestion();

            // Act
            quiz.GetNextQuestion();
        }

        [TestMethod]
        public void AnswerQuestion_ShouldReturnPlayersAnswer()
        {
            // Arrange
            string playerName = "Test Player";
            var questions = new List<Question>();

            Question question = new Question("Question 1");
            questions.Add(question);
            question.AddAnswer(new Answer("Answer 1", true));
            question.AddAnswer(new Answer("Answer 2", false));

            Quiz quiz = Quiz.Create(playerName, questions);
            QuizQuestion nextQuestion = quiz.GetNextQuestion();

            // Act
            Answer answer = quiz.AnswerQuestion(nextQuestion.QuizQuestionId, nextQuestion.OriginalQuestion.Answers.First().AnswerId);

            // Assert
            Assert.IsNotNull(answer);
            Assert.AreEqual("Answer 1", answer.Text);
        }

        [TestMethod]
        [ExpectedException(typeof(Exception), "There is no Active Question")]
        public void AnswerQuestion_ShouldThrowExceptionIfNoActiveQuestion()
        {
            // Arrange
            string playerName = "Test Player";
            var questions = new List<Question>();

            Question question = new Question("Question 1");
            questions.Add(question);
            question.AddAnswer(new Answer("Answer 1", true));
            question.AddAnswer(new Answer("Answer 2", false));

            Quiz quiz = Quiz.Create(playerName, questions);

            // Act
            quiz.AnswerQuestion("invalidQuizQuestionId", "invalidAnswerId");
        }

        [TestMethod]
        [ExpectedException(typeof(Exception), "You are not answering Active Question")]
        public void AnswerQuestion_ShouldThrowExceptionIfAnsweringNonActiveQuestion()
        {
            // Arrange
            string playerName = "Test Player";
            var questions = new List<Question>();

            Question question = new Question("Question 1");
            questions.Add(question);
            question.AddAnswer(new Answer("Answer 1", true));
            question.AddAnswer(new Answer("Answer 2", false));

            Quiz quiz = Quiz.Create(playerName, questions);
            QuizQuestion nextQuestion = quiz.GetNextQuestion();

            // Act
            quiz.AnswerQuestion("invalidQuizQuestionId", "invalidAnswerId");
        }
    }
}