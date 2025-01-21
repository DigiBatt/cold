
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WorkpieceManufacturingModule import WorkpieceManufacturing







class ArchetypeManufacturing(WorkpieceManufacturing):
    """
    Class representing the `ArchetypeManufacturing` entity, which inherits from:
    - WorkpieceManufacturing

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_e9244742_c185_4c50_b455_c57654852582'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ArchetypeManufacturing'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ArchetypeManufacturing(
    
    class_iri='https://w3id.org/emmo#EMMO_e9244742_c185_4c50_b455_c57654852582',
    
    class_name='ArchetypeManufacturing',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_e9244742_c185_4c50_b455_c57654852582',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ArchetypeManufacturing',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    