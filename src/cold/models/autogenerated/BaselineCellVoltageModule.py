
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CellVoltageModule import CellVoltage



from .ElectrochemicalControlQuantityModule import ElectrochemicalControlQuantity







class BaselineCellVoltage(CellVoltage, ElectrochemicalControlQuantity):
    """
    Class representing the `BaselineCellVoltage` entity, which inherits from:
    - CellVoltage, ElectrochemicalControlQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_269ddd97_1437_4545_b272_0df75a12c68a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'BaselineCellVoltage'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = BaselineCellVoltage(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_269ddd97_1437_4545_b272_0df75a12c68a',
    
    class_name='BaselineCellVoltage',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_269ddd97_1437_4545_b272_0df75a12c68a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'BaselineCellVoltage',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    