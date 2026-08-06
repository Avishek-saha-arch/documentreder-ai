import { useState, useEffect } from "react";
import UploadBox from "../components/UploadBox";
import DocumentCard from "../components/DocumentCard";
import { uploadDocument, getDocuments } from "../api/api";

export default function Home() {
  const [file, setFile] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [message, setMessage] = useState("");
  const [documents, setDocuments] = useState([]);

  const loadDocuments = async () => {
    try {
      const data = await getDocuments();
      setDocuments(data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    loadDocuments();
  }, []);

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first.");
      return;
    }

    try {
      setUploading(true);
      setMessage("");

      const result = await uploadDocument(file);

      setMessage(result.message);

      // Refresh document list
      await loadDocuments();

    } catch (error) {
      console.error(error);

      if (error.response) {
        setMessage(error.response.data.detail);
      } else {
        setMessage("Cannot connect to the backend.");
      }
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="min-h-screen bg-slate-100">

      <div className="max-w-5xl mx-auto p-8">

        <h1 className="text-4xl font-bold text-center">
          AI Document Reader
        </h1>

        <p className="text-center text-gray-500 mt-2">
          Upload your documents and let AI extract information.
        </p>

        <UploadBox onFileSelect={setFile} />

        {file && (
          <div className="bg-white mt-8 rounded-xl p-5 shadow">

            <h2 className="font-semibold">
              Selected File
            </h2>

            <p>{file.name}</p>

            <p className="text-gray-500">
              {(file.size / 1024 / 1024).toFixed(2)} MB
            </p>

            <button
              onClick={handleUpload}
              disabled={uploading}
              className="
                mt-5
                bg-blue-600
                text-white
                px-6
                py-3
                rounded-lg
                hover:bg-blue-700
                disabled:bg-gray-400
              "
            >
              {uploading ? "Uploading..." : "Upload Document"}
            </button>

          </div>
        )}

        {message && (
          <div className="mt-6 bg-green-100 border border-green-300 text-green-700 p-4 rounded-lg">
            {message}
          </div>
        )}

        <h2 className="text-2xl font-bold mt-10">
          Uploaded Documents
        </h2>

        {documents.length === 0 ? (
          <p className="text-gray-500 mt-4">
            No documents uploaded yet.
          </p>
        ) : (
          documents.map((doc) => (
            <DocumentCard
              key={doc.id}
              document={doc}
            />
          ))
        )}

      </div>

    </div>
  );
}