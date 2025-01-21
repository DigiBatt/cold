
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EncodedDataModule import EncodedData



from .SignModule import Sign







class Information(EncodedData, Sign):
    """
    Class representing the `Information` entity, which inherits from:
    - EncodedData, Sign

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_64c72d00_7582_44ea_a0b5_3a14e50acc36'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Information'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Information(
    
    class_iri='https://w3id.org/emmo#EMMO_64c72d00_7582_44ea_a0b5_3a14e50acc36',
    
    class_name='Information',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_64c72d00_7582_44ea_a0b5_3a14e50acc36',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Information',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    