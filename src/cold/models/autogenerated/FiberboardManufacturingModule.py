
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingFromChipModule import FormingFromChip







class FiberboardManufacturing(FormingFromChip):
    """
    Class representing the `FiberboardManufacturing` entity, which inherits from:
    - FormingFromChip

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d700aed9_2eb9_4e26_ba30_81cc36157fb1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FiberboardManufacturing'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FiberboardManufacturing(
    
    class_iri='https://w3id.org/emmo#EMMO_d700aed9_2eb9_4e26_ba30_81cc36157fb1',
    
    class_name='FiberboardManufacturing',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d700aed9_2eb9_4e26_ba30_81cc36157fb1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FiberboardManufacturing',
        alias="class_name"
    )
    

    
    

    

    