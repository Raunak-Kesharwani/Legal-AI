from backend.utils.util import cap_chunks , truncate_text
from backend.utils.sheme import ChunkLegalResponse , FinalLegalResponse
from backend.utils.prompt import chunk_prompt , merge_prompt
from backend.utils.chunker import TextSplitter



class LegalSummarizer:
    def __init__(self, model, text: str):
        self.base_model = model
        self.text = text

    def summarize(self) -> FinalLegalResponse:
        chunks = TextSplitter(self.text).summary_split()

        chunks = cap_chunks(chunks, max_chunks=9)

        chunk_model = self.base_model.with_structured_output(ChunkLegalResponse)

        chunk_results = []
        for chunk in chunks:
            result = (chunk_prompt | chunk_model).invoke(
                {"text": chunk}
            )
            chunk_results.append(result)

        merged_input = "\n\n".join(
        f"SUMMARY:\n{r.Summary}\nRISK:\n{r.Flag or 'None'}"
        for r in chunk_results
        )

        merged_input = truncate_text(merged_input, max_chars=8000)


        final_model = self.base_model.with_structured_output(FinalLegalResponse)

        final_result = (merge_prompt | final_model).invoke(
            {"text": merged_input}
        )

        return final_result
