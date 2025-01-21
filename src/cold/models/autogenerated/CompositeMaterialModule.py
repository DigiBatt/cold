
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ClassicallyDefinedMaterialModule import ClassicallyDefinedMaterial







class CompositeMaterial(ClassicallyDefinedMaterial):
    """
    Class representing the `CompositeMaterial` entity, which inherits from:
    - ClassicallyDefinedMaterial

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_f678173d_f036_4df1_a86b_2894560be617'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CompositeMaterial'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CompositeMaterial(
    
    class_iri='https://w3id.org/emmo#EMMO_f678173d_f036_4df1_a86b_2894560be617',
    
    class_name='CompositeMaterial',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_f678173d_f036_4df1_a86b_2894560be617',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CompositeMaterial',
        alias="class_name"
    )
    

    
    

    

    