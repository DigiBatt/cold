
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AblationModule import Ablation







class SparkErosion(Ablation):
    """
    Class representing the `SparkErosion` entity, which inherits from:
    - Ablation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_b8ce01a5_1e0c_4c69_8e54_7235fd4fe47e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SparkErosion'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SparkErosion(
    
    class_iri='https://w3id.org/emmo#EMMO_b8ce01a5_1e0c_4c69_8e54_7235fd4fe47e',
    
    class_name='SparkErosion',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_b8ce01a5_1e0c_4c69_8e54_7235fd4fe47e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SparkErosion',
        alias="class_name"
    )
    

    
    

    

    