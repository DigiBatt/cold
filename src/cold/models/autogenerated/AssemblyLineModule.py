
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ManufacturingSystemModule import ManufacturingSystem







class AssemblyLine(ManufacturingSystem):
    """
    Class representing the `AssemblyLine` entity, which inherits from:
    - ManufacturingSystem

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d64920b5_acd0_4e29_893e_ae03b3d7cdaf'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AssemblyLine'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AssemblyLine(
    
    class_iri='https://w3id.org/emmo#EMMO_d64920b5_acd0_4e29_893e_ae03b3d7cdaf',
    
    class_name='AssemblyLine',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d64920b5_acd0_4e29_893e_ae03b3d7cdaf',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AssemblyLine',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    