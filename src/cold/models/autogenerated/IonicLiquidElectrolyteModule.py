
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NonAqueousElectrolyteModule import NonAqueousElectrolyte







class IonicLiquidElectrolyte(NonAqueousElectrolyte):
    """
    Class representing the `IonicLiquidElectrolyte` entity, which inherits from:
    - NonAqueousElectrolyte

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c3f4b34a_0e2c_46f3_baab_4ebd2682d26f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'IonicLiquidElectrolyte'`
        - **Alias**: `class_name`
    
    - `dbpediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `dbpediaReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = IonicLiquidElectrolyte(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c3f4b34a_0e2c_46f3_baab_4ebd2682d26f',
    
    class_name='IonicLiquidElectrolyte',
    
    dbpediaReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_c3f4b34a_0e2c_46f3_baab_4ebd2682d26f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'IonicLiquidElectrolyte',
        alias="class_name"
    )
    
    dbpediaReference: Optional[str] = Field(
        None,
        alias="dbpediaReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    