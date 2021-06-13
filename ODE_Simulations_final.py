{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "ODE Simulations_final",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "TPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AYUSH19VERMA/Pipeline-_Project/blob/main/ODE_Simulations_final.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "0CNWnfyjgKNd"
      },
      "source": [
        "import matplotlib\n",
        "matplotlib.use('tkagg')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8GbTfFvQIqYE"
      },
      "source": [
        "import numpy as np\n",
        "import scipy.integrate as spi\n",
        "import matplotlib.pyplot as plt\n",
        "%matplotlib inline"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "e3t1CLg8V8r4"
      },
      "source": [
        "**Simulated short-term dynamics of response to A. fumigatus challenge in immunocompetent host with initial concentration of F given by Fo=1e6**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CVrvKVfDgqbA",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "outputId": "4045dbd0-9236-4e8a-9dc6-0ba8ced7e82f"
      },
      "source": [
        "import numpy as np\n",
        "from scipy.integrate import odeint\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "y0 = [1e6, 0, 0, 0]\t              #initial conditions \n",
        "t = np.linspace(0, 48, 1000)      #x-axis scale\n",
        "\n",
        "\n",
        "alpha = 0.0017                   #equation parameters \n",
        "beta = 0.28\n",
        "k_NF = 1.2e-6\n",
        "d_MF = 0.32e-6\n",
        "k_C = 0.38e-12\n",
        "k_CD = 0.31e-6\n",
        "delta_C = 0.066\n",
        "delta_N = 0.061\n",
        "alpha_D_Dv = 0.017e6\t          # alpha_D*Dv taken together\n",
        "k_ND = 0.0069e-6\n",
        "delta_D = 0.1\n",
        "\n",
        "\n",
        "params = [alpha, beta, k_NF, d_MF, k_C, k_CD, delta_C, delta_N, alpha_D_Dv, k_ND, delta_D]        #passing parameters to params\n",
        "\n",
        "def sim(variables, t, params):\n",
        "\tF = variables[0]\t\n",
        "\tC = variables[1]   \n",
        "\tN = variables[2]\n",
        "\tD = variables[3]   \n",
        "\tNv =  150e6                 # value of Nv reamins constant \n",
        "                              # Dv = variable[5] taken with alpha_D  \n",
        "\tM = 0.3e6                   # value of M remains constant\n",
        "\talpha = params[0]\n",
        "\tbeta = params[1]\n",
        "\tk_NF = params[2]\n",
        "\td_MF = params[3]\n",
        "\tk_C = params[4]\n",
        "\tk_CD = params[5]\n",
        "\tdelta_C = params[6]\n",
        "\tdelta_N = params[7]\n",
        "\talpha_D_Dv = params[8]\n",
        "\tk_ND = params[9]\n",
        "\tdelta_D = params[10]\n",
        "\n",
        "\n",
        "\tdFdt = beta*F - k_NF*N*F - d_MF*M*F\n",
        "\tdCdt = k_C*M*F + k_CD*D - delta_C*C\n",
        "\tdNdt = alpha*Nv*C - k_NF*N*F - delta_N*N \n",
        "\tdDdt = alpha_D_Dv*C - k_ND*N*D - delta_D*D\n",
        "\n",
        "\treturn([dFdt, dCdt, dNdt, dDdt]) \n",
        "\n",
        "\n",
        "y = odeint(sim, y0, t, args=(params,))          # getting values of F,C,N,D\n",
        "a1 = y[:,0]                                     # a1 contains the solution of F       \n",
        "a2 = y[:,1]                                     # a2 contains the solution of C     \n",
        "a3 = y[:,2]                                     # a3 contains the solution of N     \n",
        "a4 = y[:,3]                                     # a4 contains the solution of D     \n",
        "\n",
        "plt.plot(t,a1, label = 'F', color ='blue',)      # plotting F with blue colour\n",
        "plt.plot(t,a2*1e6, color ='cyan', label = 'C')  # plotting C with cyan colour\n",
        "plt.plot(t,a3, color ='red',label = 'N')        # plotting N with red colour\n",
        "plt.plot(t,a4, color ='pink', label = 'D')      # plotting D with pink colour\n",
        "plt.yscale(\"log\",)\n",
        "plt.ylim(1e4,1e7)                               # plotting range on y-axis\n",
        "ticks1 = [0,24,48]                              # plotting interval on x-axis\n",
        "plt.xticks([0,24,48],ticks1)                    \n",
        "\n",
        "\n",
        "plt.xlabel(\"Time[h]\")\n",
        "plt.ylabel(\"Cells\")\n",
        "plt.title(\"Immunocompetent\")\n",
        "\n",
        "plt.grid()\n",
        "\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "GGkhoMeKnzCM"
      },
      "source": [
        "**Simulated short-term dynamics of response to A. fumigatus challenge in immunocompetent host with initial concentration of F given by Fo=1e4**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "id": "vU5XdPX1oF30",
        "outputId": "8e084f0e-f0e4-4cd6-c896-93214d4f0947"
      },
      "source": [
        "import numpy as np\n",
        "from scipy.integrate import odeint\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "y0 = [1e4, 0, 0, 0]\t              #initial conditions \n",
        "t = np.linspace(0, 72, 1000)      #x-axis scale\n",
        "\n",
        "\n",
        "alpha = 0.0017                   #equation parameters \n",
        "beta = 0.28\n",
        "k_NF = 1.2e-6\n",
        "d_MF = 0.32e-6\n",
        "k_C = 0.38e-12\n",
        "k_CD = 0.31e-6\n",
        "delta_C = 0.066\n",
        "delta_N = 0.061\n",
        "alpha_D_Dv = 0.017e6\t          # alpha_D*Dv taken together\n",
        "k_ND = 0.0069e-6\n",
        "delta_D = 0.1\n",
        "\n",
        "\n",
        "params = [alpha, beta, k_NF, d_MF, k_C, k_CD, delta_C, delta_N, alpha_D_Dv, k_ND, delta_D]        #passing parameters to params\n",
        "\n",
        "def sim(variables, t, params):\n",
        "\tF = variables[0]\t\n",
        "\tC = variables[1]   \n",
        "\tN = variables[2]\n",
        "\tD = variables[3]   \n",
        "\tNv =  150e6                 # value of Nv reamins constant \n",
        "                              # Dv = variable[5] taken with alpha_D  \n",
        "\tM = 0.3e6                   # value of M remains constant\n",
        "\talpha = params[0]\n",
        "\tbeta = params[1]\n",
        "\tk_NF = params[2]\n",
        "\td_MF = params[3]\n",
        "\tk_C = params[4]\n",
        "\tk_CD = params[5]\n",
        "\tdelta_C = params[6]\n",
        "\tdelta_N = params[7]\n",
        "\talpha_D_Dv = params[8]\n",
        "\tk_ND = params[9]\n",
        "\tdelta_D = params[10]\n",
        "\n",
        "\n",
        "\tdFdt = beta*F - k_NF*N*F - d_MF*M*F\n",
        "\tdCdt = k_C*M*F + k_CD*D - delta_C*C\n",
        "\tdNdt = alpha*Nv*C - k_NF*N*F - delta_N*N \n",
        "\tdDdt = alpha_D_Dv*C - k_ND*N*D - delta_D*D\n",
        "\n",
        "\treturn([dFdt, dCdt, dNdt, dDdt]) \n",
        "\n",
        "\n",
        "y = odeint(sim, y0, t, args=(params,))          # getting values of F,C,N,D\n",
        "a1 = y[:,0]                                     # a1 contains the solution of F       \n",
        "a2 = y[:,1]                                     # a2 contains the solution of C     \n",
        "a3 = y[:,2]                                     # a3 contains the solution of N     \n",
        "a4 = y[:,3]                                     # a4 contains the solution of D     \n",
        "\n",
        "plt.plot(t,a1, label = 'F', color ='blue',)      # plotting F with blue colour\n",
        "plt.plot(t,a2*1e6, color ='cyan', label = 'C')  # plotting C with cyan colour\n",
        "plt.plot(t,a3, color ='red',label = 'N')        # plotting N with red colour\n",
        "plt.plot(t,a4, color ='pink', label = 'D')      # plotting D with pink colour\n",
        "plt.yscale(\"log\",)\n",
        "plt.ylim(1e0,1e7)                               # plotting range on y-axis\n",
        "ticks1 = [0,24,48,72]                              # plotting interval on x-axis\n",
        "plt.xticks([0,24,48,72],ticks1)                    \n",
        "\n",
        "\n",
        "plt.xlabel(\"Time[h]\")\n",
        "plt.ylabel(\"Cells\")\n",
        "plt.title(\"Immunocompetent\")\n",
        "\n",
        "plt.grid()\n",
        "\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ZDlyEzEXn21a"
      },
      "source": [
        "**Simulated short-term dynamics of response to A. fumigatus challenge in immunocompetent host with initial concentration of F given by Fo=1e2**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "id": "S22RwkoQoms7",
        "outputId": "4197bc09-a850-4fc1-8889-6394f5240d57"
      },
      "source": [
        "import numpy as np\n",
        "from scipy.integrate import odeint\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "y0 = [1e2, 0, 0, 0]\t              #initial conditions \n",
        "t = np.linspace(0, 72, 1000)      #x-axis scale\n",
        "\n",
        "\n",
        "alpha = 0.0017                   #equation parameters \n",
        "beta = 0.28\n",
        "k_NF = 1.2e-6\n",
        "d_MF = 0.32e-6\n",
        "k_C = 0.38e-12\n",
        "k_CD = 0.31e-6\n",
        "delta_C = 0.066\n",
        "delta_N = 0.061\n",
        "alpha_D_Dv = 0.017e6\t          # alpha_D*Dv taken together\n",
        "k_ND = 0.0069e-6\n",
        "delta_D = 0.1\n",
        "\n",
        "\n",
        "params = [alpha, beta, k_NF, d_MF, k_C, k_CD, delta_C, delta_N, alpha_D_Dv, k_ND, delta_D]        #passing parameters to params\n",
        "\n",
        "def sim(variables, t, params):\n",
        "\tF = variables[0]\t\n",
        "\tC = variables[1]   \n",
        "\tN = variables[2]\n",
        "\tD = variables[3]   \n",
        "\tNv =  150e6                 # value of Nv reamins constant \n",
        "                              # Dv = variable[5] taken with alpha_D  \n",
        "\tM = 0.3e6                   # value of M remains constant\n",
        "\talpha = params[0]\n",
        "\tbeta = params[1]\n",
        "\tk_NF = params[2]\n",
        "\td_MF = params[3]\n",
        "\tk_C = params[4]\n",
        "\tk_CD = params[5]\n",
        "\tdelta_C = params[6]\n",
        "\tdelta_N = params[7]\n",
        "\talpha_D_Dv = params[8]\n",
        "\tk_ND = params[9]\n",
        "\tdelta_D = params[10]\n",
        "\n",
        "\n",
        "\tdFdt = beta*F - k_NF*N*F - d_MF*M*F\n",
        "\tdCdt = k_C*M*F + k_CD*D - delta_C*C\n",
        "\tdNdt = alpha*Nv*C - k_NF*N*F - delta_N*N \n",
        "\tdDdt = alpha_D_Dv*C - k_ND*N*D - delta_D*D\n",
        "\n",
        "\treturn([dFdt, dCdt, dNdt, dDdt]) \n",
        "\n",
        "\n",
        "y = odeint(sim, y0, t, args=(params,))          # getting values of F,C,N,D\n",
        "a1 = y[:,0]                                     # a1 contains the solution of F       \n",
        "a2 = y[:,1]                                     # a2 contains the solution of C     \n",
        "a3 = y[:,2]                                     # a3 contains the solution of N     \n",
        "a4 = y[:,3]                                     # a4 contains the solution of D     \n",
        "\n",
        "plt.plot(t,a1, label = 'F', color ='blue',)      # plotting F with blue colour\n",
        "plt.plot(t,a2*1e6, color ='cyan', label = 'C')  # plotting C with cyan colour\n",
        "plt.plot(t,a3, color ='red',label = 'N')        # plotting N with red colour\n",
        "plt.plot(t,a4, color ='pink', label = 'D')      # plotting D with pink colour\n",
        "plt.yscale(\"log\",)\n",
        "plt.ylim(1e0,1e7)                               # plotting range on y-axis\n",
        "ticks1 = [0,24,48,72]                              # plotting interval on x-axis\n",
        "plt.xticks([0,24,48,72],ticks1)                    \n",
        "\n",
        "\n",
        "plt.xlabel(\"Time[h]\")\n",
        "plt.ylabel(\"Cells\")\n",
        "plt.title(\"Immunocompetent\")\n",
        "\n",
        "plt.grid()\n",
        "\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tl5nvzBQWZfU"
      },
      "source": [
        "**Simulated short-term dynamics of response to A. fumigatus challenge in neutropenic hosts with initial concentration of F given by Fo=1e6**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "B1TVqkMYnF99",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "outputId": "d19f369e-da03-4457-88f8-3600c3b4a687"
      },
      "source": [
        "import numpy as np\n",
        "import matplotlib\n",
        "from scipy.integrate import odeint\n",
        "matplotlib.use('tkagg')\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "y0 = [1e6, 0, 0, 0]\t\n",
        "t = np.linspace(0, 48, 1000)\n",
        "alpha = 0.0017\n",
        "beta = 0.28\n",
        "k_NF = 1.2e-6\n",
        "d_MF = 0.32e-6\n",
        "k_C = 0.38e-12\n",
        "k_CD = 0.31e-6\n",
        "delta_C = 0.066\n",
        "delta_N = 0.061\n",
        "alpha_D_Dv = 0.017e6\t      # Dv is included in alpha_D*Dv\n",
        "k_ND = 0.0069e-6\n",
        "delta_D = 0.1\n",
        "\n",
        "\n",
        "params = [alpha, beta, k_NF, d_MF, k_C, k_CD, delta_C, delta_N, alpha_D_Dv, k_ND, delta_D]\n",
        "\n",
        "def sim(variables, t, params):\n",
        "\tF = variables[0]\t\n",
        "\tC = variables[1]    \n",
        "\tN = variables[2]\n",
        "\tD = variables[3]    \n",
        "\tNv =  150e6*0.1            \n",
        "        # Dv = variable[5] taken with alpha_D  \n",
        "\tM = 0.3e6      \n",
        "\n",
        "\talpha = params[0]\n",
        "\tbeta = params[1]\n",
        "\tk_NF = params[2]\n",
        "\td_MF = params[3]\n",
        "\tk_C = params[4]\n",
        "\tk_CD = params[5]\n",
        "\tdelta_C = params[6]\n",
        "\tdelta_N = params[7]\n",
        "\talpha_D_Dv = params[8]\n",
        "\tk_ND = params[9]\n",
        "\tdelta_D = params[10]\n",
        "\n",
        "\n",
        "\tdFdt = beta*F - k_NF*N*F - d_MF*M*F\n",
        "\tdCdt = k_C*M*F + k_CD*D - delta_C*C\n",
        "\tdNdt = alpha*Nv*C - k_NF*N*F - delta_N*N \n",
        "\tdDdt = alpha_D_Dv*C - k_ND*N*D - delta_D*D\n",
        "\n",
        "\treturn([dFdt, dCdt, dNdt, dDdt]) \n",
        "\n",
        "y = odeint(sim, y0, t, args=(params,))          # getting values of F,C,N,D\n",
        "a1 = y[:,0]                                     # a1 contains the solution of F       \n",
        "a2 = y[:,1]                                     # a2 contains the solution of C     \n",
        "a3 = y[:,2]                                     # a3 contains the solution of N     \n",
        "a4 = y[:,3]                                     # a4 contains the solution of D     \n",
        "\n",
        "plt.plot(t,a1, label = 'F', color ='blue',)      # plotting F with blue colour\n",
        "plt.plot(t,a2*1e6, color ='cyan', label = 'C')  # plotting C with cyan colour\n",
        "plt.plot(t,a3, color ='red',label = 'N')        # plotting N with red colour\n",
        "plt.plot(t,a4, color ='pink', label = 'D')      # plotting D with pink colour\n",
        "plt.yscale(\"log\",)\n",
        "plt.ylim(1e4,1e7)                               # plotting range on y-axis\n",
        "ticks1 = [0,24,48]                              # plotting interval on x-axis\n",
        "plt.xticks([0,24,48],ticks1)     \n",
        "\n",
        "\n",
        "plt.xlabel(\"Time[h]\")\n",
        "plt.ylabel(\"Cells\")\n",
        "plt.title(\"Neutropenic\")\n",
        "\n",
        "plt.grid()\n",
        "\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYUAAAEWCAYAAACJ0YulAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nO3deXzcVb3/8denaZM23dJ9b9M2XSgti/SCgFyiCJSlbCIXRPEi3gqIiIKCygXl6u/qBQRELlAF670qCIoiiEK5UlsEka3QQvc9TdM0bZo2+zLn98eZtCFNmm2+853vzPv5eOQxS2bmfNpM5pOzfY455xAREQHoFXYAIiKSOpQURETkACUFERE5QElBREQOUFIQEZEDlBREROQAJQWRiDOzh8zs38OOQ9KDaZ+CpAsz2wzkApOdc1Xx+z4PfNo5V9jD13bANOfc+p7GKZLK1FOQdJMFfDnZjZpZ72S3KRIEJQVJN3cCN5lZXutvmNlMM1tsZnvMbI2ZXdLie0vivYrm2/9qZi/Hry+N3/2OmVWa2b+YWaGZFZnZzWZWAvzMzHLM7F4zK45/3WtmOfHXaH78N82szMw2m9nlLdrLMbO7zGyrme2MDwn1a/XcG82s1Mx2mNmVLZ67yMy+2+L2+Wa23Mz2mdkGM5uXsP9dSXtKCpJu3gCWADe1vNPM+gOLgV8BI4FLgf82s1kdvaBz7p/jV492zg1wzv06fns0MBSYBCwAvgV8GDgGOBo4Hri1xUuNBoYD44DPAgvNbEb8e98HpsefWxB/zG2tnjs4fv9VwANmNqR1rGZ2PPA/wNeAPOCfgc0d/RtFmikpSDq6DfiSmY1ocd+5wGbn3M+cc43OubeB3wKf7EE7MeB251ydc64GuBy4wzlX6pzbBXwH+Eyr5/x7/PF/Bf4IXGJmhk8qX3HO7XHO7Qf+Hz5xNWuIv3aDc+45oBKYwaGuAh51zi12zsWcc9udc6t78G+UDKNxUEk7zrmVZvYscAuwKn73JOAEM9vb4qG9gf/tQVO7nHO1LW6PBba0uL0lfl+z8uYJ8FbfH4GfIH/T5wcADD8/0my3c66xxe1qYEAbMU0AnuvKP0KkJSUFSVe3A28Bd8dvbwP+6pw7vZ3HV+E/mJuN7kQbrZfuFeOTz3vx2xPj9zUbYmb9WySGicBKoAyoAY50zm3vRLuHsw2Y2sPXkAym4SNJS/Glo78Gro/f9Sww3cw+Y2Z94l//ZGZHxL+/HLjIzHLNrAA/DNPSTmBKB80+BtxqZiPMbDh+GOsXrR7zHTPLNrNT8ENaTzrnYsBPgHvMbCSAmY0zszO7/i/nEeBKMzvNzHrFX2dmN15HMpSSgqSzO4D+APFx+jPw4/TFQAnwAyAn/th7gHr8h//PgV+2eq1vAz83s70tVy218l38RPe7wAp8T+W7Lb5fApTH2/8lcHWL8f6bgfXA381sH/Aibc8ZHJZz7h/AlfF/TwXwV3zvRaRTtHlNJAnMrBD4hXNufNixiByOegoiInJAykw0x8dYL8fHNMs5d1LIIYmIZJxAh4/M7FH8ZFqpc252i/vnAffhl9z91Dn3/RbfuwAY5Zx7OLDARESkTUEPHy0CPrDF3syygAeAs4BZwGWtdpV+Cr/rVEREkizQ4SPn3FIzy2919/HAeufcRgAzexw4H3jfzCYCFfGVIm0yswX43Z/069fvuAkTJnQrtlgsRq9emlLpibq6XmzfnktTkzFmTA0DBjR2/KRuKM3JYW92NgMaGxlTU4N1/JTQpfv7KwujX/wnUYOj6ZAtGxK0nrzH1q5dW+acG9HW98KYUxiH32DTrAg4IX79KuBnh3uyc24hsBBg7ty57o033uhWEEuWLKGwsLBbzxVYvBguvhiGD4dnnoG5cxPfRi1wBfAkcAN+F1pUPmbT+v21owzWbYF+OTB7mr+UpOvJe8zMtrT3vZSZaAZwzt0edgzSsYUL4dprYdYsePZZmDgx8W3sBS7AL7K/C7gx8U1IVzkHm7bDthIYMghmTYHeKfURIgkQxk90O74+S7Px8fskxcVicMstcOedMG8e/PrXMGhQ4tspwk9ErcVPLl2W+Cakq5pisHoTlJXDmBFQMAHSeHgsk4WRFF4HppnZZHwyuBQ/udxpZjYfmF9QUBBAeNKW6mr4zGfgqafgmmvgRz8K5o/ElfgVCBXAn4GPJb4J6ar6Bli5HvZXwZTxMH4UWBRmdqQ7Ak31ZvYY8CowI35IyFXxSo/XAc/jK1g+4Zx773Cv05pz7hnn3ILBgwcnPmg5REkJFBbC734HP/whPPBAMAlhKXAK0AQsQwkhJVTVwNur/OWRU2HCaCWENBf06qM2e/7xevAq7xsBK1fCOedAWZlPCuefH0w7v8HvXJyM7yHkB9OMdEX5PnhvA/QyOHoGDOofdkSSBJEcFDSz+Wa2sKKiIuxQ0toLL8DJJ0NDAyxdGlxCuB+4BJgL/A0lhJSwYxesWAc5feBDRyghZJBIJgUNHwXv4Yfh7LMhPx9eew2OOy7xbcTwp+BcD5yHLws6LPHNSFc4BxuLYO0WyBsIx86EvlpymkkimRQkOLEY3HQTXH01nHEGvPwydHN/4GHV4w8p/gFwNf5czH6Jb0a6oikGqzb6JadjhsPsAi05zUD6icsB1dXw6U/7uYMvfhHuvTeYz4Qq4BP4lQbfBb4JkdilnNa0wkjilBQE8CuM5s+HN9/0yeD664P5TNgNnINfl/wT4POJb0K6qqoGVq6D+kaYNRVGDAk7IglRJJOC9ikkVssVRr//PZx3XjDtbAPOBDbih4suCKYZ6YoPrDCaDoMGhB2RhCyScwqaaE6c55+Hk07yK4yWLQsuIawCTsLvVnweJYSUUFLWaoWREoJENClIYjz0kO8hTJ7sVxh96EPBtPMa8BGgAV/L6NRgmpHOcg42FcGazVphJIdQUshATU1+hdE118CZZwa3wgh8r+BjQB5+D8IxwTQjndW8wmhrCYzWCiM5VCSTgjavdV9VlS95fffdcN118PTTMHBgMG09hj92bxo+IUwNphnprPoGeHcN7CqHyeNg+iQVtZNDRPIdoTmF7tmxA0491SeC++6D++8P7o/EH+GrHJ6EHzIaHUwz0lnVNfD2aqis9iWvJ47RklNpk/qNGeLdd+Hcc2HPHp8U5s8Pph0H3Ibff3ABvrfQN5impLPK98H7G3wSOHqGJpTlsJQUMsCf/wyXXOKHiZYtg2OPDaadJuBa/LF4VwEPoTdY6ErKfMkKnZImnRTJ4SPpvAcf9D2EqVP9CqOgEkId8C/4hPBN/MY0JYQQNZ+StmYzDB7gVxgpIUgn6Pc2TTU1wde/7s8/OOcceOyx4CaUq/BDRS8C9+DPU5YQxWKwejPs2uNXGE2bqAll6bRIJgXtaD68qiq4/HI/d/ClL/nEENSEcjm+bMVrwCJ8kTsJUX0DvLce9lX5FUY6FEe6KJJ/Pmj1UfuKi/0Ko2ee8SuMgjo2E2An8FHgDeBJlBBCV13rVxjt1woj6b5I9hSkbe++64eKyst9L+Hcc4NraytwOr6e0bPAGcE1JZ2xN17DyAyO0Qoj6T4lhTTxpz/5FUaDBgW7wghgLfBxYB+wGDg5uKakM7TCSBIoksNH8kEPPeR7BQUF8I9/BJsQ3gFOAWqBl1BCCJVzsLnFCqNjtMJIek5JIcJiMfja13wNo7PO8j2EceOCa+9VoBDIBpYCAeYe6UgsBqs3wZYdfoXRnGnQRx1/6Tm9iyKqpgauuAJ+8xu49lo/qRxkXbMX8ctOx8SvTwquKelIQ6M/JW1fpVYYScJFMilk+pLUXbvg/PPh73/3he2+8pVgPxN+j9+YNgN4AdUxClVNrT8DobYejpgCI4eGHZGkmUgOH2XyktS1a+HDH4a334Ynn4SvfjXYhPAr4GL8UNESlBBCVVHpl5w2NPpT0pQQJACR7ClkqmXL4IILICsLXnrJJ4cgLQI+hz8U5w9AQBuipTN2lcPqjZCd7ecPclVmUIIRyZ5CJnr8cfj4x2H4cHj11eATwkLgSvzS0z+ihBAa52Bbia9yOiDX1zBSQpAAKSmkOOfgP/8TLrsMTjjBJ4SpAZ9Wcz/wBeBsfA8hN9jmpD3OwfqtsLEIhg+Bo2ZAdp+wo5I0p+GjFNbQ4FcW/fSn8KlPwaOPQk7Ay9DvAr6GX2n0OKBV7yFpaoL3N8KeChg/CqaM1wojSQolhRS1bx988pPwwgtw661wxx3BfyZ8D7gVuAT4BaC/SUNSV++XnFZWQ8FEGDcy7IgkgygppKCiIjj7bFi1Ch55BD73uWDbc8DtwH8AnwZ+ht4Yoamq8UtOGxphdgEMyws7Iskw+t1PMcuX+6J2lZXw3HNw+unBtueAW4D/wk8s/wTICrZJaU95vKhdVi9f1G5g/7AjkgwUyYlmM5tvZgsrKirCDiWh/vQnOOUUv+T05ZeTkxBuxCeEq4GfooQQmpIy30PI6eNXGCkhSEgimRTScfPaww/D/PkwbZrfqTxnTrDtNSeEe4AvAf9NRN8MUeccbC7+4LGZfTW9L+HR50DIYjG4+Wa4+mqYNw+WLoWxY4Nt0wFfxyeE64D7AK1rCUEs5pPBlmIYNcxvSguygJVIJ+gdGKKaGvjsZ325imuuCfaUtGYO+AZ+6em1wI9QQghFY6OfP9i7HyaNhUk6JU1Sg5JCSMrKfFG7V16Bu+4KvoYR+ITwLeAHwDXAj1FCCEVtnZ8/qKmDGfm+9LVIilBSCMG6dX7JaVGR7yVcfHHwbTrgNuA/gQUoIYRmf5Xfg9AU88NFQwaFHZHIBygpJNkrr8B55/leQTKK2jX7DvBd4PPAg2gyKRS79/pdyn16+wnl/v3CjkjkEPpsSKKnnoLTToOhQ/0Ko2QlhDvwSeFzwMPohx6K7aW+h5DbFz50hBKCpCx9PiTJ/ff7YaJjjvG9haCL2jW7E79b+V/xG9P0A08y52DDNl/YbthgvylNRe0khekzImCxGNx0E1x/vZ9Y/r//8+Wvk+FB/NLTS/Eb0/TDTrJYDFZthKKdMHYkHFngdyaKpDDNKQSottYvOX3iCbjuOrj33uR9JvwvfsnpfOB/0E7lZOsN8M5af47ylPG+0qmWnEoEKCkEpLzcn5K2dCnceSfceGPyPhN+h69jdBrwBKp2mnS1dRxLrl9ppHOUJWKUFAKwZQucdRZs2ACPPQaXXpq8tp8H/gU4Afg9oDO6kmx/NaxcRzYGR02HPJ1ZJ9ESyWHmVC6It3w5nHgiFBfD888nNyEsBS4EjsQfoTkgeU0L+ANx3lkNZrxNjRKCRFIkk0KqFsR74QVf5bR3b/jb36CwMHltvwGcC0wCXgBUhT/Jmquc9s2BY2dSTSzsiES6JZJJIRUtWuTPQZgyxZ+jfOSRyWt7HXAWMAx4ERiRvKalZZXTvIFwzEzIyQ47KpFuU1LoIef8UZlXXul7BsuWwbhxyWt/B3Bm/PrzQBKbFudg7ZZWVU61zkuiTRPNPdDQ4KubPvIIXHEF/OQnkJ3EPxIr8D2EUuAlYHrympamJl+yYk8FTBwD+WO15FTSgpJCN1VWwiWX+NPSbr3V9xaS+ZlQC1wAvIefVP6n5DUt9Q1+/qCyGqZNgrEasJP0oaTQDTt3+iqny5f7E9MWLEhu+03AZ4AlwC+AM5LbfGarroUVa6G+EWYXwDBN6Ut6UVLoovXr4cwzoaQEnn4azj03ue074MvAb/AH5Vye3OYzW0UlrFznu4RHT4dBWvQr6UdJoQveestvSmtqgr/8BU44Ifkx3Ak8ANyEP2NZkmRXOaze6FcWzZkG/bQtUNKTVh910osvwqmnQt++fg9CGAnhN8DNwCX409MkSbbvhPc3QP9cv+RUCUHSmJJCJzz+uJ9DyM/3Za9nzEh+DK/h5xFOBBahH1xSHCh7vc3PHRw9XWWvJe3ps6UD990Hl13mS1ckew9Cs83AecAY4GlAx7MkQSwGqzfFy16PgCOnquy1ZAQlhXY4B9/4BtxwA1x4oa9jlBfCQpMK4BygDr/0VIsfk6CxyZ+SVroH8sdBwUTtQZCMoYnmNjQ0+GWmixbBF74ADzwQzh+JDcAngbX43cpHJD+EzNNyD8KMfBidpBORRFKEkkIr1dV+U9of/wjf/jbcdlt4fyR+BVgMPAJ8LJwQMktNLby7zicG7UGQDKWk0MLu3X7fwT/+AQ8+CFdfHV4sj+CXnt4IfC68MDLH/irfQ3DOn4MwWHsQJDMpKcRt3eo3pW3aBE8+CRddFF4sf8cfpXk68P3wwsgc5fvgvfW+5vmcadBfU/mSuZQUgJUrfUKorPQTyqeeGl4sxcBFwHjgcfQDClzpHr/KKLevTwgqey0ZLuM/c5Ytg/POg379/PWjjgovljrgE8A+/MSyTvYNWNFOvw9h8AA4sgD6ZPyvg0jqJAUz6wX8BzAIeMM59/Og23z6aX9c5sSJvoeQnx90i+1zwBfxQ0e/AeaEF0r6cw42bYdtJTA8D2ZOgSytzhaBgPcpmNmjZlZqZitb3T/PzNaY2XozuyV+9/n4UZMGoCjIuACefXYMF13kewZ/+1u4CQHgZ/jJ5W/hewsSkFjMn5K2rQTGjIBZU5UQRFoI+rdhETCv5R1mloVfWHMWMAu4zMxmATOAV5xzXwWuCTKoe+6Bu++ewRln+MJ2w0Neir4C30s4DfhOuKGkt6YmP6G8czdMGgvTtClNpLVAh4+cc0vNLL/V3ccD651zGwHM7HF8L2EbUB9/TFN7r2lmC4AFAKNGjWLJkiVdjis3dyDz5g3nxhs38/rrrsvPT6TqrCyuPu44crOyuPaNN1jW0BBqPOmqDzCHfgykF2upY8fmtbB5bWDtVVZWduu9KdJZQb3HwphTGIdPAM2KgBOA+4D7zewUYGl7T3bOLQQWAsydO9cVFhZ2OYDCQpgxYwndeW4iOfx5CNuBvwCnnnxyqPGkrdo6vymtrg6OmMKM4UMIuqbhkiXhv78kvQX1HkuZiWbnXDVwVdhxJNNC4DHge0CIq2DTW1WNPymtMQZzpkPewLAjEklpYcywbQcmtLg9Pn5fp5nZfDNbWFFRkdDAkmkl/gS1ecAtHTxWumlfFSxfAzEHx8xQQhDphDCSwuvANDObbGbZwKXAH7ryAs65Z5xzCwYPHhxIgEGrww8bDQZ+jkrVBqJ8H7y7Bnr3gmNnwoDcsCMSiYSgl6Q+BrwKzDCzIjO7yjnXCFyH35+1CnjCOfdekHGkmm8B7+KXoY4MOZa0tKvc1zHqm6OT0kS6KOjVR5e1c/9zwHNBtp2q/g+4G1/b6OyQY0lLO3bB2i0wqD/MnqZdyiJdFMmRi6jOKewBPgvMBO4MOZa0tK3EJ4Qhg3ylUyUEkS6LZFKI6pzCF4FS4JeARrgTyDnYWOS/RgzxZyHo6EyRbtGfUknyNL7q6R3Ah0KOJa0453sHJWW+bIV2KYv0iJJCEpTj63YcjZafJlQsBqs2QtlemDgG8scqIYj0UCSTgpnNB+YXFBSEHUqn3IgfNnoWX25BEqAxXsdo736YOgHGjwo7IpG0oDmFgD2PX3r6dTRslDANjfDuWp8QZuQrIYgkUCR7ClFRBXwBv9rotpBjSRv1DT4hVNfCkVNh+JCwIxJJK0oKAfoesAVf3U/bpxKgrh7eWesvZxfA0NTvKYpEjZJCQNYAdwFXAKeEHEtaqKnzZSsaGv1ZyqpjJBKISM4ppPrmNQd8Cb8X4b9CjiUtVNXA8tV+cvloFbYTCVIkk0KqTzT/FlgMfBfQFGgPVVbDO2v8foRjZsLA/mFHJJLWNHyUYNXAV4BjgKtDjiXy9lX6wnZZWb5sRa5mZkSCpqSQYPfgj5L7FfrP7ZHyfbByPeT08Qmhb07YEYlkBH1uJVAp8APgAjS53CO798L7G3wiOGo65GSHHZFIxlBSSKDv4IePvh92IFG2q9yXrujfD46aBn20B1wkmSI50ZyKq4/WAA/jN6sFfSh82ird43sIA3Ph6OlKCCIhiGRSSMXVR9/EL0G9PexAomrnbt9DGDwA5kyH3urEioQhkkkh1bwNPIUvfKfjNbuhpAxWb/L7D+ZMg946C0EkLPpzLAHuAPKAL4cdSBTtKIO1m31C0OE4IqFTT6GH3gZ+j9+bkBdyLJFTvMsnhCGD/HnKSggioetUUjCzqWaWE79eaGbXm5k+AznYS7g+7ECiZnsprNvii9rNLoAs/X0ikgo6+5v4W6DJzAqAhcAE/P6sjPYO6iV0S9FOWL8VhuX58te9lBBEUkVnfxtjzrlG4ELgfufc14AxwYV1eKmyJPVuoD+++J100rYS2LANhufBrClKCCIpprO/kQ1mdhnwWfypkhDiyZKpsCS1CHgMuArQMS+dtK0ENhbBiCFwhBKCSCrq7G/llcCJwPecc5vMbDLwv8GFlfruB2LADWEHEhVFO5UQRCKgU0tSnXPv02Iu1Tm3CV/mJyPtx+9e/gQwOeRYImF7aXzIaAjMnAxmYUckIu04bFIwsxX4M2Pa5Jw7KuERRcAjQAV+s5p0oHjXwUnlIyarhyCS4jrqKZyblCgixAEPACcBJ4QcS8orKTu47FSTyiKRcNik4JzbkqxAomIJsB64LeQ4Ut7O3bBms9+YpmWnIpHR0fDRfg4OHzUPBLv4deecGxRgbCnpYfxqo4vDDiSVle4+WMvoyAIlBJEI6ainoBPSW9iFL3x3LdAv5FhS1q49sGqTr3aqncoikdPp31gz+4iZXRm/Pjy+LDUUYW1eWwQ04M9MkDaU7fUJYdAAX+1UtYxEIqeztY9uB24GvhG/Kxv4RVBBdSSMzWsOeBT4CHBE0lqNkPJ9/oCcAblKCCIR1tmewoXAeUAVgHOuGMiooaW3gNXAFWEHkor2VcLK9ZDbV+chiERcZ5NCvXPOEZ90NrP+wYWUmn6J7x5pgrmVympYsQ6y+/iE0EdHdIhEWWeTwhNm9jCQZ2b/BrwI/CS4sFJLE/A4cDaqc/QB1bXw7lo/mXz0dMjJDjsiEemhjpakFgCjnHN3mdnpwD78ufR/Ap5LQnwp4SVgB3B52IGkkto6nxAAjpoOfXPCjUdEEqKjvv69xCeXnXOLgcUAZjYn/r35gUaXIh7HT6CcE3YgqaK+wSeExiY4egbkaoGuSLroaPholHNuRes74/flBxJRimkC/oCv96GPPqCx0SeEugaYUwADc8OOSEQSqKOkcLgDxTLiM/JV/Ka188MOJBXEYn6VUXWtL10xOKMWoIlkhI6SwhvxieUPMLPPA28GE1JqeRp/mtBZYQcSNudg1UaoqPTlr4eGd8CRiASnozmFG4DfmdnlHEwCc/GrMy8MMrBU4PBnMH8MyLgiTy05B+u2+h3LUyfAyKFhRyQiAemo9tFO4CQz+ygwO373H51zfwk8shSwCl8R9athBxK2rTtgxy6YMBrGjwo7GhEJUGdPXnsJvzIzozQfRn1eqFGEbMcu2FwMo4bB5HFhRyMiAYtkCctkFcRbjO8eZexHYdleWLsFhg6C6ZN0jKZIBohkUkhGQbwaYBlwemAtpLiKSli1AQb2h1k6JEckU+g3vR0vA3XAx8MOJAzVtX7paU6234ugiqciGUNJoR0v4peinhp2IMnW0Agr1/mz9eZMgz59wo5IRJJISaEdi4GTgIwqBxuLwXvrobbeH6PZr2/YEYlIkikptGEvsBz4aNiBJJNzsGbzwc1pgweEHZGIhEBJoQ2v4TeufSTsQJJpSzGU7oH8cdqcJpLBlBTa8Df8f8zxYQeSLCVlsGWH34swcXTY0YhIiJQU2vAKcDQZct7o3v1+L0LeQO1FEBElhdYa8cNHJ4UdSDLU1sH7G/wBOdqLICIoKRxiBVBJBiSFpia/FyHmYHaBzlYWEUBJ4RCvxC9PDjWKgDkHqzdDVQ3MmgK5WnoqIp6SQitvAiOAiWEHEqStO6CsHKaM17kIIvIBSgqtLAeOxW/oTUtl5b7q6cihKoMtIodQUmihHlgJHBN2IEGpqoHVm/y5ytPztdJIRA6hpNDC+0ADvqeQdhoa/cRyVpYvYZGlH72IHEqfDC0sj1+mXVJwDtZsgrp6v/Q0JzvsiEQkRSkptPA2kAsUhB1Iom0rgd0VMHW8ahqJyGGlTFIws0IzW2ZmD5lZYRgxrADmAGl1ekD5Pti0HUYMhbEjw45GRFJcoEnBzB41s1IzW9nq/nlmtsbM1pvZLfG7HX7fWF+gKMi42rMaOCKMhoNSVw+rNvp9CDNUwkJEOhZ0T2ERMK/lHWaWBTwAnAXMAi4zs1nAMufcWcDNwHcCjusQFcAOYGayGw5KLAbvb4SmmJ9H0OlpItIJgdY2cM4tNbP8VncfD6x3zm0EMLPHgfOdc+/Hv18O5LT3mma2AFgAMGrUKJYsWdKt2CorKz/w3FUDB8Jxx9GwYgVLdu/u1mumkqlkM8Gyec/Vsuv118IOJ+O0fn+JJFpQ77EwCt6MA7a1uF0EnGBmFwFnAnnAj9t7snNuIbAQYO7cua6wsLBbQSxZsoSWz90av7x4zpzo9xZ27/XLT8eO5Mhpab03O2W1fn+JJFpQ77GUqYLmnHsKeCqs9lfj/zOmhhVAotTV+xPUBvTzq41ERLogjNVH24EJLW6Pj98XqjX4hBDpY+qd8zuWm2JwhEphi0jXhfGp8Towzcwmm1k2cCnwh668gJnNN7OFFRUVCQtqNWkwyby1xB+aM22iKp+KSLcEvST1MeBVYIaZFZnZVc65RuA64HlgFfCEc+69rryuc+4Z59yCwYMTU+EzBmwApiXk1UJSUQmb4/sRRg0LOxoRiaigVx9d1s79zwHPBdl2V+wE6oDJYQfSXY2Nfj9C32yYPlH7EUSk2yI56Jzo4aPN8cv8hLxaCNZt9RPMR0yB3imzdkBEIiiSSSHRw0eb45f5CXm1JNtVDqV7YNIYGKS6RiLSM5FMCom2OX45KcwguqO+AdZtgQG5MHFM2NGISBpQUsAnhRFA/5Dj6BLnYO0WaGyCmZO1/FREEkKfJPikkB9yDF22c7ffuTx5HPTvF3Y0IpImIpkUEj3RvJWIDR3V1sH6bf5sBJ2zLCIJFMmkkOiJ5mJgbEJeKQmah42cgxmTtfxURBIqkkkhkaqBfV7OBwAAAArcSURBVEBkpml37vYH50wZD/3aLSYrItItGZ8UdsQvI5EU6htgwzYY1B/Gjgg7GhFJQ5FMComcU4hUUtiwzRe7m56vYSMRCUQkk0Ii5xSK45cpnxR27/Wb1CaO0WojEQlMJJNCIkWip9DY5EtZ5PaFiaPDjkZE0piSAv4MhZSuK7p5u69tND1fm9REJFAZ/wmzAxgNpOwIfWU1bC+FMSP8vgQRkQBlfFIoIYWHjpzzw0a9e/udyyIiAYtkUkjk6qMyfN2jlFS6B/ZVwpRx0EclsUUkeJFMColcfbQHGNrzkBKvsQk2FsHAXBg9POxoRCRDRDIpJFLKJoXNxX6zWsEk7UkQkaTJ6KTQgC9xkXJJoaoGtu+EMcP97mURkSTJ6KSwN345JNQo2rCxCLKyNLksIkmX0UmhPH6ZUj2F8n2wp8Ifr9mnT9jRiEiGyeiksCd+mTJJwTlf36hvNowbGXY0IpKBIpkUErUkNeWSws7dfj5h8njtXBaRUETykydRS1JTKik0NcGm7TCwP4xIuVkOEckQkUwKiZJSSaFop1+COnW8lqCKSGiUFIC8UKMAGhph204YlgeDB4YdjYhksIxPCnlAVtiBFJX44aP8yJwULSJpKuOTQuij9/UNUFQKI4bCgNywoxGRDJfRSWE/0PPqST20rQRiMfUSRCQlZHRSqARCPaGgrh6KS2HUMH+qmohIyDI6Kewn5KSwdQc4YJJ6CSKSGiKZFBK1ea0SCG2tT1097CiD0cOgX05YUYiIfEAkk0KiNq+FOnxUtNOXtZiYsue+iUgGimRSSJTQkkJDIxTvgpFDoa96CSKSOpQUwmh4+06/4ki9BBFJMRmbFBrMaCCEpNDUBNtL/e7l/v2S3bqIyGFlbFKoyfL7mJOeFIp3+fOXJ45OdssiIh1SUkhmo7GYn2DOGwiDQl0MKyLSJiWFZDa6q9yXtRivXoKIpCYlhWQ16JyfYM7tC0MHJatVEZEuyfik0D9ZDe6rhP3V/phNnZcgIikqY5NCffy4y6St/9leCr2zfJ0jEZEUlfFJISlbx2rr/HzC6OGQFfrpDSIi7crYpNCQzKRQvMtfjhuZjNZERLotkkkhEQXxkpYUYjFf+G54nkpaiEjKi2RSSERBvPr4ZG/gpxiU7YXGRhgzIuiWRER6LJJJIRGS1lPYsQv6ZsMQLUMVkdSnpBBkI9W1sHc/jB6hZagiEglKCkE2UlLmL0drGaqIREPGJoX6Xr3oBfQOqoFYzCeF4XmQkx1UKyIiCZWxSaHBLNhewu69/jAdTTCLSIRkbFKo79Ur4KGj3ZDTRxPMIhIpGZsUGoJMCvUNsKcCRg7TBLOIRIqSQhBK9/hL1TkSkYjJ3KQQ5JxC6W4Y0E/HbYpI5GRuUgiqp1Bd40tkj1QvQUSiJ2OTQn2vXsGUuNgZHzoaOTSIVxcRCVRGJ4WE9xSc80NHQwZpb4KIRFLGJoVAho/2V0NtvXoJIhJZmZsUgphoLiv3S1CH5SX6lUVEkiJzk0KiewrO+dPV8gZCn8CKZ4iIBCpjP70SnhSqavyxmxNHJ/JVJd045+tiNTV179K5rn9193k9+Wr9b27r/0GP6fxj2tAvO5h5y4xNCgmfaN5V7i81dBQc56CuDmpqoLbWX6+tPfT64b5XVwcNDQe/Ght7fruND++P1Nf7ocS2PtRFEmDwzTcH8roplRTMrD/wV+Dbzrlng2yryYw+iXzBsvjQUXZCXzX6nPMf4uXlsHev/2p5vaICKisPflVVtX29+XZTU8/i6dUL+vT54Ffv3h3f7tu37e9nZR386tXrwPUdxcVMmDTp4H2JuOzVyyearn5193k9/WqprXIvekzXHtNK6cqVzDzsI7on0KRgZo8C5wKlzrnZLe6fB9wHZAE/dc59P/6tm4EngoypWZMZWYl6saoaf6DO2JGJesXU1dQEZWVQWnr4r927D37wNzQc/jWzs2HAAOjf/4OXY8cevN58f//+kJvrP6T79oWcnLavt3e7d3L+DtqwZAkTCguT0pZkptiGDYG8btC/IYuAHwP/03yHmWUBDwCnA0XA62b2B2Ac8D5JODYZIAaJSwple/3l8DQYOiovhw0bYOtWKCqCbdv8V/P14mI/ZNJaVhaMGAEjR/qvSZNgyBDIy/Nfzddb3zdokE8KIpISzAU8xmlm+cCzzT0FMzsRPzx0Zvz2N+IPHQD0B2YBNcCFzrlYG6+3AFgQvzkDWNPN0IYDZd18rkhH9P6SoPXkPTbJOdfmYS9hzCmMA7a1uF0EnOCcuw7AzP4VKGsrIQA45xYCC3sahJm94Zyb29PXEWmL3l8StKDeYyk10QzgnFsUdgwiIpkqjM1r24EJLW6Pj98nIiIhCyMpvA5MM7PJZpYNXAr8IYQ4ejwEJXIYen9J0AJ5jwU60WxmjwGF+AmRncDtzrlHzOxs4F78AqBHnXPfCywIERHptMBXH4mISHRkbEE8ERE5VEYmBTObZ2ZrzGy9md0SdjwSbWY2wcxeMrP3zew9M/tyq+/faGbOzIaHFaNEn5llmdnbZvZs/PZpZvaWmS03s5fNrCAR7WRcUmixo/os/Ea5y8xsVrhRScQ1Ajc652YBHwa+2PyeMrMJwBnA1hDjk/TwZWBVi9sPApc7544BfgXcmohGMi4pAMcD651zG51z9cDjwPkhxyQR5pzb4Zx7K359P/4Xd1z82/cAXwc0eSfdZmbjgXOAn7a42wGD4tcHA8WJaCvlNq8lQZs7qkOKRdJMvKzLscBrZnY+sN059451UPFSpAP34v+4GNjivs8Dz5lZDbAP30vtsUzsKYgEwswGAL8FbsAPKX0TuC3UoCTyzKy50vSbrb71FeBs59x44GfADxPRXib2FLSjWhLOzPrgE8IvnXNPmdkcYDLQ3EsYD7xlZsc750pCDFWi52TgvPj+rr7AIDP7IzDTOfda/DG/Bv6ciMYybp+CmfUG1gKn4ZPB68CnnHPvhRqYRJb5T/2fA3uccze085jNwFznnCqnSreZWSFwE3ABUAKc5Jxba2ZX4XsNn+hpGxnXU3DONZrZdcDzHNxRrYQgPXEy8BlghZktj9/3TefccyHGJGks/jn2b8BvzSwGlAOfS8RrZ1xPQURE2qeJZhEROUBJQUREDlBSEBGRA5QURETkACUFERE5QElBREQOUFIQiTOzYfEyxMvNrMTMtsevV5rZfyeojSXxsu3ntbg9t43HnRIvxb0yEe2KdFbGbV4TaY9zbjdwDICZfRuodM7dFUBTlzvn3ugglmXxsgbPBtC+SLvUUxDpgJkVtjjY5Ntm9nMzW2ZmW8zsIjP7LzNbYWZ/jtdAwsyOM7O/mtmbZva8mY05TBOfNLN/mNlaMzslKf8okXYoKYh03VTgY8B5wC+Al5xzc4Aa4Jx4YrgfuNg5dxzwKPC9w7xeb+fc8fjqqrcHGrlIBzR8JNJ1f3LONZjZCnz9rObqlCuAfGAGMBtYHK+QmgXsOMzrPRW/fDP+fJHQKCmIdF0dgHMuZmYN7mABsRj+d8qA95xzJ3bl9YAm9DspIdPwkUjirQFGmNmJ4M9aMLMjQ45JpFOUFEQSLH7298XAD8zsHWA5cFK4UYl0jkpniySRmS0BbupoSWr8sfnAs8652QGHJXKAegoiybUHWNS8ea098aWpzwA6qU2SSj0FERE5QD0FERE5QElBREQOUFIQEZEDlBREROSA/w/89n4iPZvCXQAAAABJRU5ErkJggg==\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xJs7eybkXKJf"
      },
      "source": [
        "**Timing-dependent effects of neutrophil depletion on fungal clearance time for immunocompetent host**\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7-Lx1H5oFPH5",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "outputId": "01c2a2a0-36d7-4b76-df99-d80dfba76f52"
      },
      "source": [
        "import numpy as np\n",
        "import matplotlib\n",
        "from scipy.integrate import odeint\n",
        "import matplotlib.pyplot as plt\n",
        "y0 = [1e6, 0, 0, 0]\t              #initial conditions \n",
        "\n",
        "t1 = np.linspace(0, 21, 1000)\n",
        "t2 = np.linspace(21, 48, 1000)\n",
        "alpha = 0.0017                   #equation parameters \n",
        "beta = 0.28\n",
        "k_NF = 1.2e-6\n",
        "d_MF = 0.32e-6\n",
        "k_C = 0.38e-12\n",
        "k_CD = 0.31e-6\n",
        "delta_C = 0.066\n",
        "delta_N = 0.061\n",
        "alpha_D_Dv = 0.017e6\t          # alpha_D*Dv taken together\n",
        "k_ND = 0.0069e-6\n",
        "delta_D = 0.1\n",
        "\n",
        "\n",
        "params = [alpha, beta, k_NF, d_MF, k_C, k_CD, delta_C, delta_N, alpha_D_Dv, k_ND, delta_D]  #passing parameters to param\n",
        "\n",
        "#for generating solution for the ODES for time interval 0 to 21\n",
        "def sim1(variables, t, params):\n",
        "\t\n",
        "  F = variables[0]\n",
        "  C = variables[1]\n",
        "  N = variables[2]\n",
        "  D = variables[3]\n",
        "  M = 0.3e6                     # M remains constant\n",
        "  Nv = 150e6\n",
        "  alpha = params[0]\n",
        "  beta = params[1]\n",
        "  k_NF = params[2]\n",
        "  d_MF = params[3]\n",
        "  k_C = params[4]\n",
        "  k_CD = params[5]\n",
        "  delta_C = params[6]\n",
        "  delta_N = params[7]\n",
        "  alpha_D_Dv = params[8]\n",
        "  k_ND = params[9]\n",
        "  delta_D = params[10]\n",
        "\n",
        "\n",
        "  dFdt = beta*F - k_NF*N*F - d_MF*M*F\n",
        "  dCdt = k_C*M*F + k_CD*D - delta_C*C\n",
        "  dNdt = alpha*Nv*C - k_NF*N*F - delta_N*N \n",
        "  dDdt = alpha_D_Dv*C - k_ND*N*D - delta_D*D\n",
        "\n",
        "  return([dFdt, dCdt, dNdt, dDdt]) \n",
        "# for generating solution for time interval 21 to 48\n",
        "def sim2(variables, t, params):\n",
        "\tF = variables[0]\t\n",
        "\tC = variables[1]    \n",
        "\tN = variables[2]\n",
        "\tD = variables[3]\n",
        "\tM = 0.3e6         # M remains constant\n",
        "\tNv = 15e6         # due to 90% Nv depletion after 20hours post-inoculation  \n",
        "\talpha = params[0]\n",
        "\tbeta = params[1]\n",
        "\tk_NF = params[2]\n",
        "\td_MF = params[3]\n",
        "\tk_C = params[4]\n",
        "\tk_CD = params[5]\n",
        "\tdelta_C = params[6]\n",
        "\tdelta_N = params[7]\n",
        "\talpha_D_Dv = params[8]\n",
        "\tk_ND = params[9]\n",
        "\tdelta_D = params[10]\n",
        "\n",
        "\n",
        "\tdFdt = beta*F - k_NF*N*F - d_MF*M*F\n",
        "\tdCdt = k_C*M*F + k_CD*D - delta_C*C\n",
        "\tdNdt = alpha*Nv*C - k_NF*N*F - delta_N*N \n",
        "\tdDdt = alpha_D_Dv*C - k_ND*N*D - delta_D*D\n",
        "\n",
        "\treturn([dFdt, dCdt, dNdt, dDdt]) \n",
        "\n",
        "\n",
        "y1 = odeint(sim1, y0, t1, args=(params,))           # getting values of F,C,N,D from time interval 0 to 21\n",
        "y2 = odeint(sim2, y1[-1], t2, args=(params,))       # getting values of F,C,N,D from time interval 21 to 48\n",
        "\n",
        "a1 = list(y1[:,0])+list(y2[:,0])                    # merging the values obtained from two intervals for F\n",
        "a1 = np.asarray(a1, dtype=np.float32)\n",
        "\n",
        "a2 = list(y1[:,1])+list(y2[:,1])                    # merging the values obtained from two intervals for C\n",
        "a2 = np.asarray(a2, dtype=np.float32)\n",
        "\n",
        "a3 = list(y1[:,2])+list(y2[:,2])                    # merging the values obtained from two intervals for N\n",
        "a3 = np.asarray(a3, dtype=np.float32)\n",
        "\n",
        "a4 = list(y1[:,3])+list(y2[:,3])                    # merging the values obtained from two intervals for D\n",
        "a4 = np.asarray(a4, dtype=np.float32)\n",
        "\n",
        "\n",
        "t = list(t1)+list(t2)                             # combinig time intervals\n",
        "#print((y1[:,0]),(a1))\n",
        "plt.plot(t,a1, label = 'F', color ='blue',)      # plotting F with blue colour\n",
        "plt.plot(t,a2*1e6, color ='cyan', label = 'C')  # plotting C with cyan colour\n",
        "plt.plot(t,a3, color ='red',label = 'N')        # plotting N with red colour\n",
        "plt.plot(t,a4, color ='pink', label = 'D')      # plotting D with pink colour\n",
        "plt.yscale(\"log\",)\n",
        "plt.ylim(1e4,1e7)                               # plotting range on y-axis\n",
        "ticks1 = [0,24,48]                              # plotting interval on x-axis\n",
        "plt.xticks([0,24,48],ticks1) \n",
        "\n",
        "\n",
        "plt.xlabel(\"Time[h]\")\n",
        "plt.ylabel(\"Cells\")\n",
        "plt.title(\"Immunocompetent\")\n",
        "\n",
        "plt.grid()\n",
        "\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "NTbnIGinWw55"
      },
      "source": [
        "**Timing-dependent effects of neutrophil depletion on fungal clearance time for neutropenic host**\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pNcTYhBFIrZJ",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "outputId": "03a6b848-f48b-47df-f675-6465bfa43bc2"
      },
      "source": [
        "import numpy as np\n",
        "import matplotlib\n",
        "from scipy.integrate import odeint\n",
        "import matplotlib.pyplot as plt\n",
        "y0 = [1e6, 0, 0, 0]\t              #initial conditions \n",
        "\n",
        "t1 = np.linspace(0, 21, 1000)\n",
        "t2 = np.linspace(21, 48, 1000)\n",
        "alpha = 0.0017                   #equation parameters \n",
        "beta = 0.28\n",
        "k_NF = 1.2e-6\n",
        "d_MF = 0.32e-6\n",
        "k_C = 0.38e-12\n",
        "k_CD = 0.31e-6\n",
        "delta_C = 0.066\n",
        "delta_N = 0.061\n",
        "alpha_D_Dv = 0.017e6\t          # alpha_D*Dv taken together\n",
        "k_ND = 0.0069e-6\n",
        "delta_D = 0.1\n",
        "\n",
        "\n",
        "params = [alpha, beta, k_NF, d_MF, k_C, k_CD, delta_C, delta_N, alpha_D_Dv, k_ND, delta_D]  #passing parameters to param\n",
        "\n",
        "#for generating solution for the ODES for time interval 0 to 21\n",
        "def sim1(variables, t, params):\n",
        "\t\n",
        "  F = variables[0]\n",
        "  C = variables[1]\n",
        "  N = variables[2]\n",
        "  D = variables[3]\n",
        "  M = 0.3e6                     # M remains constant\n",
        "  Nv = 15e6 # due to 90% Nv depletion at 0h\n",
        "  alpha = params[0]\n",
        "  beta = params[1]\n",
        "  k_NF = params[2]\n",
        "  d_MF = params[3]\n",
        "  k_C = params[4]\n",
        "  k_CD = params[5]\n",
        "  delta_C = params[6]\n",
        "  delta_N = params[7]\n",
        "  alpha_D_Dv = params[8]\n",
        "  k_ND = params[9]\n",
        "  delta_D = params[10]\n",
        "\n",
        "\n",
        "  dFdt = beta*F - k_NF*N*F - d_MF*M*F\n",
        "  dCdt = k_C*M*F + k_CD*D - delta_C*C\n",
        "  dNdt = alpha*Nv*C - k_NF*N*F - delta_N*N \n",
        "  dDdt = alpha_D_Dv*C - k_ND*N*D - delta_D*D\n",
        "\n",
        "  return([dFdt, dCdt, dNdt, dDdt]) \n",
        "# for generating solution for time interval 21 to 48\n",
        "def sim2(variables, t, params):\n",
        "\tF = variables[0]\t\n",
        "\tC = variables[1]    \n",
        "\tN = variables[2]\n",
        "\tD = variables[3]\n",
        "\tM = 0.3e6 # M remains constant\n",
        "\tNv = 15e6   \n",
        "\talpha = params[0]\n",
        "\tbeta = params[1]\n",
        "\tk_NF = params[2]\n",
        "\td_MF = params[3]\n",
        "\tk_C = params[4]\n",
        "\tk_CD = params[5]\n",
        "\tdelta_C = params[6]\n",
        "\tdelta_N = params[7]\n",
        "\talpha_D_Dv = params[8]\n",
        "\tk_ND = params[9]\n",
        "\tdelta_D = params[10]\n",
        "\n",
        "\n",
        "\tdFdt = beta*F - k_NF*N*F - d_MF*M*F\n",
        "\tdCdt = k_C*M*F + k_CD*D - delta_C*C\n",
        "\tdNdt = alpha*Nv*C - k_NF*N*F - delta_N*N \n",
        "\tdDdt = alpha_D_Dv*C - k_ND*N*D - delta_D*D\n",
        "\n",
        "\treturn([dFdt, dCdt, dNdt, dDdt]) \n",
        "\n",
        "\n",
        "y1 = odeint(sim1, y0, t1, args=(params,))           # getting values of F,C,N,D from time interval 0 to 21\n",
        "y2 = odeint(sim2, y1[-1], t2, args=(params,))       # getting values of F,C,N,D from time interval 21 to 48\n",
        "\n",
        "a1 = list(y1[:,0])+list(y2[:,0])                    # merging the values obtained from two intervals for F\n",
        "a1 = np.asarray(a1, dtype=np.float32)\n",
        "\n",
        "a2 = list(y1[:,1])+list(y2[:,1])                    # merging the values obtained from two intervals for C\n",
        "a2 = np.asarray(a2, dtype=np.float32)\n",
        "\n",
        "a3 = list(y1[:,2])+list(y2[:,2])                    # merging the values obtained from two intervals for N\n",
        "a3 = np.asarray(a3, dtype=np.float32)\n",
        "\n",
        "a4 = list(y1[:,3])+list(y2[:,3])                    # merging the values obtained from two intervals for D\n",
        "a4 = np.asarray(a4, dtype=np.float32)\n",
        "\n",
        "\n",
        "t = list(t1)+list(t2)                             # combinig time intervals\n",
        "#print((y1[:,0]),(a1))\n",
        "plt.plot(t,a1, label = 'F', color ='blue',)      # plotting F with blue colour\n",
        "plt.plot(t,a2*1e6, color ='cyan', label = 'C')  # plotting C with cyan colour\n",
        "plt.plot(t,a3, color ='red',label = 'N')        # plotting N with red colour\n",
        "plt.plot(t,a4, color ='pink', label = 'D')      # plotting D with pink colour\n",
        "plt.yscale(\"log\",)\n",
        "plt.ylim(1e4,1e7)                               # plotting range on y-axis\n",
        "ticks1 = [0,24,48]                              # plotting interval on x-axis\n",
        "plt.xticks([0,24,48],ticks1) \n",
        "\n",
        "\n",
        "plt.xlabel(\"Time[h]\")\n",
        "plt.ylabel(\"Cells\")\n",
        "plt.title(\"Neutropenic\")\n",
        "\n",
        "plt.grid()\n",
        "\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "zq_HEiGJMNn7"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}