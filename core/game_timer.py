import time
from typing import Optional

class GameTimer:
    """Handles game timing and stopwatch functionality"""
    
    def __init__(self):
        self._start_time: Optional[float] = None
        self._pause_time: Optional[float] = None
        self._total_paused_time: float = 0.0
        self._is_running: bool = False
        self._is_paused: bool = False
    
    def start(self) -> None:
        """Start the game timer"""
        if not self._is_running:
            self._start_time = time.time()
            self._is_running = True
            self._is_paused = False
            self._total_paused_time = 0.0
    
    def pause(self) -> None:
        """Pause the timer"""
        if self._is_running and not self._is_paused:
            self._pause_time = time.time()
            self._is_paused = True
    
    def resume(self) -> None:
        """Resume the timer from pause"""
        if self._is_paused and self._pause_time:
            self._total_paused_time += time.time() - self._pause_time
            self._pause_time = None
            self._is_paused = False
    
    def stop(self) -> float:
        """Stop the timer and return total elapsed time"""
        if not self._is_running:
            return 0.0
        
        if self._is_paused and self._pause_time:
            self._total_paused_time += time.time() - self._pause_time
        
        self._is_running = False
        self._is_paused = False
        return self.get_elapsed_time()
    
    def get_elapsed_time(self) -> float:
        """Get current elapsed time in seconds"""
        if not self._start_time:
            return 0.0
        
        if self._is_paused and self._pause_time:
            return self._pause_time - self._start_time - self._total_paused_time
        
        if self._is_running:
            return time.time() - self._start_time - self._total_paused_time
        
        return 0.0
    
    def get_formatted_time(self) -> str:
        """Get formatted time as MM:SS"""
        elapsed = self.get_elapsed_time()
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        return f"{minutes:02d}:{seconds:02d}"
    
    def get_detailed_time(self) -> str:
        """Get detailed formatted time as HH:MM:SS"""
        elapsed = self.get_elapsed_time()
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = int(elapsed % 60)
        
        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        return f"{minutes:02d}:{seconds:02d}"
    
    def is_running(self) -> bool:
        """Check if timer is currently running"""
        return self._is_running and not self._is_paused
    
    def is_paused(self) -> bool:
        """Check if timer is currently paused"""
        return self._is_paused
    
    def reset(self) -> None:
        """Reset the timer to initial state"""
        self._start_time = None
        self._pause_time = None
        self._total_paused_time = 0.0
        self._is_running = False
        self._is_paused = False
