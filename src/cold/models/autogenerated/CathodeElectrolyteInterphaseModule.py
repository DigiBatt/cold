
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SolidElectrolyteInterphaseModule import SolidElectrolyteInterphase







class CathodeElectrolyteInterphase(SolidElectrolyteInterphase):
    """
    Class representing the `CathodeElectrolyteInterphase` entity, which inherits from:
    - SolidElectrolyteInterphase

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f8e0d532_cf44_403c_9188_e00ee161a3c1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CathodeElectrolyteInterphase'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CathodeElectrolyteInterphase(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f8e0d532_cf44_403c_9188_e00ee161a3c1',
    
    class_name='CathodeElectrolyteInterphase',
    
    elucidation="example_value",
    
    comment="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_f8e0d532_cf44_403c_9188_e00ee161a3c1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CathodeElectrolyteInterphase',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    

    
    

    

    