import express from "express";
import { connectDB, getQuestions, saveQuestion } from "./db.js";

const server = express();

server.use(express.json());

connectDB();

// GET questions
async function getQuestionHandler(req, res) {
  try {
    const questions = await getQuestions();
    return res.json(questions);
  } catch (error) {
    console.error(error);
    res.status(500).json("error");
  }
}

server.get("/getQuestion", getQuestionHandler);


// SAVE questions
async function saveQuestionHandler(req, res) {

  const questions = req.body;

  for (const q of questions) {
    try {
      await saveQuestion(q);
    } catch (error) {
      console.error(error);
    }
  }

  return res.json("ok");
}

server.post("/saveQuestion", saveQuestionHandler);


function start() {
  console.log("server started on port 3000");
}

server.listen(3000, start);