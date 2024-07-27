#ifdef GL_ES
precision mediump float;
#endif

#define MAX_ITERATIONS 1000

uniform vec2 iMouse;
uniform float iTime;
uniform vec2 iResolution;

uniform float CenterX;
uniform float CenterY;
uniform float ZoomScale;
uniform vec4 ColorRanges;

varying vec2 vTexCoord;

float GetIterations()
{
    // If you change the screen, adjust the values of offset X and offset Y
    float offsetX = 1.0;
    float offsetY = 0.5;
    float real = ((gl_FragCoord.x / 1080.0 - offsetX) * ZoomScale + CenterX) * 4.0;
    float imag = ((gl_FragCoord.y / 1080.0 - offsetY) * ZoomScale + CenterY) * 4.0;

    int iterations = 0;
    float real_number = real;
    float imaginary = imag;

    while (iterations < MAX_ITERATIONS)
    {
        float tmp_real = real;
        real = (pow(real, 2.0) - pow(imag, 2.0)) + real_number;
        imag = (2.0 * tmp_real * imag) + imaginary;

        float dist = pow(real, 2.0) + pow(imag, 2.0);

        if (dist > 4.0)
        {
            break;
        }

        ++iterations;
    }
    return float(iterations);
}

vec4 GetColorValues()
{
    vec2 uv = gl_FragCoord.xy / iResolution.xy * 2.0 - 1.0;
    uv.x *= iResolution.x / iResolution.y;

    float iter = GetIterations();
    if (iter == float(MAX_ITERATIONS))
    {
        gl_FragDepth = 0.0;
        return vec4(0.001, 0.00, 0.001, 1.0);
    }

    float iterations = iter / float(MAX_ITERATIONS);
    gl_FragDepth = iterations;

    vec3 iColor = 0.5 + 0.5 * cos(iTime + uv.xyx + vec3(0.0, 2.0, 4.0));
    vec4 color_0 = vec4(0.0, 0.0, 0.0, 1.0);
    vec4 color_1 = vec4(iColor.x / 2.0, 0.5, 0.6, 1.0);
    vec4 color_2 = vec4(0.3, iColor.y, 0.4, 1.0);
    vec4 color_3 = vec4(iColor, 1.0);

    float fraction = 0.0;
    if (iterations < ColorRanges[1])
    {
        fraction = (iterations - ColorRanges[0]) / (ColorRanges[1] - ColorRanges[0]);
        return mix(color_0, color_1, fraction);
    }
    else if (iterations < ColorRanges[2])
    {
        fraction = (iterations - ColorRanges[1]) / (ColorRanges[2] - ColorRanges[1]);
        return mix(color_1, color_2, fraction);
    }
    else
    {
        fraction = (iterations - ColorRanges[2]) / (ColorRanges[3] - ColorRanges[2]);
        return mix(color_2, color_3, fraction);
    }
}

void main()
{
    vec4 color = GetColorValues();
    gl_FragColor = color;
}