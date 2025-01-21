
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingFromChipModule import FormingFromChip







class PaperManufacturing(FormingFromChip):
    """
    Class representing the `PaperManufacturing` entity, which inherits from:
    - FormingFromChip

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_123b0aee_eac2_461f_8078_3a7c8dfbe7ce'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PaperManufacturing'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PaperManufacturing(
    
    class_iri='https://w3id.org/emmo#EMMO_123b0aee_eac2_461f_8078_3a7c8dfbe7ce',
    
    class_name='PaperManufacturing',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_123b0aee_eac2_461f_8078_3a7c8dfbe7ce',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PaperManufacturing',
        alias="class_name"
    )
    

    
    

    

    