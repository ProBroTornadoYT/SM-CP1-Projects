def matrix_rainbow_typewriter(text: str, delay: float = 0.04) -> None:
    """Prints text character by character cycling through an RGB color wheel."""
    # Custom 24-bit RGB neon spectrum
    colors = [
        (255, 0, 0),    # Red
        (255, 127, 0),  # Orange
        (255, 255, 0),  # Yellow
        (0, 255, 0),    # Green
        (0, 0, 255),    # Blue
        (139, 0, 255)   # Violet
    ]
    
    for i, char in enumerate(text):
        r, g, b = colors[i % len(colors)]
        # Construct dynamic 24-bit color string
        color_code = f"\033[1;38;2;{r};{g};{b}m"
        
        sys.stdout.write(f"{color_code}{char}")
        sys.stdout.flush()
        time.sleep(delay)
        
    print(RESET) # Always cleanly exit formatting at line-end