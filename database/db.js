import mongoose from "mongoose";
import fs from "fs";

const env = JSON.parse(fs.readFileSync("./env.json"));

const DB_URL = env.DB_URL;
// Connect DB
export async function connectDB() {
  try {
    await mongoose.connect(DB_URL);
    console.log("DB connected");
  } catch (error) {
    console.error(error);
    process.exit(1);
  }
}

connectDB();

// Schema for questions
const questionSchema = new mongoose.Schema({
  content: {
    type: String,
    required: true,
    unique:true
  }
});

// Model
const Question = mongoose.model("Question", questionSchema);

// Helper functions

// Get questions 
export async function getQuestions() {
  return await Question.find();
}

// Save question
export async function saveQuestion(content) {
  const q = new Question({ content });
  return await q.save();
}

// Delete question
export async function deleteQuestion(id) {
  return await Question.findByIdAndDelete(id);
}