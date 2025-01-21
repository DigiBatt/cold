
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingFromPlasticModule import FormingFromPlastic







class TransferMolding(FormingFromPlastic):
    """
    Class representing the `TransferMolding` entity, which inherits from:
    - FormingFromPlastic

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_79575941_45dc_4f15_bb59_dc04dff2c92d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TransferMolding'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TransferMolding(
    
    class_iri='https://w3id.org/emmo#EMMO_79575941_45dc_4f15_bb59_dc04dff2c92d',
    
    class_name='TransferMolding',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_79575941_45dc_4f15_bb59_dc04dff2c92d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TransferMolding',
        alias="class_name"
    )
    

    
    

    

    