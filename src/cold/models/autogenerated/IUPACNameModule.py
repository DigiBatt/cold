
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalNameModule import ChemicalName



from .IUPACNomencaltureModule import IUPACNomencalture







class IUPACName(ChemicalName, IUPACNomencalture):
    """
    Class representing the `IUPACName` entity, which inherits from:
    - ChemicalName, IUPACNomencalture

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_16a3bd5c_75f0_42b3_b000_cb0d018f840e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IUPACName'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IUPACName(
    
    class_iri='https://w3id.org/emmo#EMMO_16a3bd5c_75f0_42b3_b000_cb0d018f840e',
    
    class_name='IUPACName',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_16a3bd5c_75f0_42b3_b000_cb0d018f840e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IUPACName',
        alias="class_name"
    )
    

    
    

    

    