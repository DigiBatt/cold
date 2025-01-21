
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .IUPACNomencaltureModule import IUPACNomencalture







class InChI(IUPACNomencalture):
    """
    Class representing the `InChI` entity, which inherits from:
    - IUPACNomencalture

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d74ed682_894f_46c5_87cb_167f60926965'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'InChI'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = InChI(
    
    class_iri='https://w3id.org/emmo#EMMO_d74ed682_894f_46c5_87cb_167f60926965',
    
    class_name='InChI',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d74ed682_894f_46c5_87cb_167f60926965',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'InChI',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    