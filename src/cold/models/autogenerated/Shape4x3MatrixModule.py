
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MatrixModule import Matrix







class Shape4x3Matrix(Matrix):
    """
    Class representing the `Shape4x3Matrix` entity, which inherits from:
    - Matrix

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_24b30ba4_90f4_423d_93d2_fd0fde349087'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Shape4x3Matrix'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Shape4x3Matrix(
    
    class_iri='https://w3id.org/emmo#EMMO_24b30ba4_90f4_423d_93d2_fd0fde349087',
    
    class_name='Shape4x3Matrix',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_24b30ba4_90f4_423d_93d2_fd0fde349087',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Shape4x3Matrix',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    