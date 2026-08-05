import { useRef } from "react";
import { Upload } from "lucide-react";

export default function UploadBox({ onFileSelect }) {
  const inputRef = useRef(null);

  const handleClick = () => {
    inputRef.current.click();
  };

  const handleChange = (e) => {
    const file = e.target.files[0];

    if (file) {
      onFileSelect(file);
    }
  };

  return (
    <div
      onClick={handleClick}
      className="
        mt-10
        border-2
        border-dashed
        border-blue-400
        rounded-xl
        p-16
        bg-white
        cursor-pointer
        hover:border-blue-600
        transition
        text-center
      "
    >
      <Upload
        size={60}
        className="mx-auto text-blue-500"
      />

      <h2 className="text-2xl font-semibold mt-5">
        Drag & Drop your document
      </h2>

      <p className="text-gray-500 mt-2">
        or click to browse
      </p>

      <p className="text-sm text-gray-400 mt-4">
        PDF • JPG • JPEG • PNG
      </p>

      <input
        type="file"
        hidden
        ref={inputRef}
        accept=".pdf,.png,.jpg,.jpeg"
        onChange={handleChange}
      />
    </div>
  );
}