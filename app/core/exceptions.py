from typing import Optional


class BranchlyException(Exception):
    """Base exception for branchly-specific errors."""
    pass


class VideoDownloadError(BranchlyException):
    """Raised when a video/audio download fails."""
    pass


class TranscriptionError(BranchlyException):
    """Raised when transcription of audio fails."""
    pass


class AssetGenerationError(BranchlyException):
    """Raised when the LLM or asset generation fails."""
    pass
