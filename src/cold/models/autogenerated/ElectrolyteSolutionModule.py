
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WholeModule import Whole



from .LiquidSolutionModule import LiquidSolution



from .LiquidElectrolyteModule import LiquidElectrolyte





from .ChemicalCompoundModule import ChemicalCompound





class ElectrolyteSolution(Whole, LiquidSolution, LiquidElectrolyte):
    """
    Class representing the `ElectrolyteSolution` entity, which inherits from:
    - Whole, LiquidSolution, LiquidElectrolyte

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_fa22874b_76a9_4043_8b8f_6086c88746de'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrolyteSolution'`
        - **Alias**: `class_name`
    
    - `hasSolvent` (`Optional[ChemicalCompound]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSolvent`
    
    - `hasSolute` (`Optional[ChemicalCompound]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSolute`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrolyteSolution(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_fa22874b_76a9_4043_8b8f_6086c88746de',
    
    class_name='ElectrolyteSolution',
    
    hasSolvent="example_value",
    
    hasSolute="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_fa22874b_76a9_4043_8b8f_6086c88746de',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrolyteSolution',
        alias="class_name"
    )
    
    hasSolvent: Optional[ChemicalCompound] = Field(
        None,
        alias="hasSolvent"
    )
    
    hasSolute: Optional[ChemicalCompound] = Field(
        None,
        alias="hasSolute"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    @validator("hasSolvent", pre=True, always=True)
    def validate_hasSolvent(cls, value):
        if value is not None and not isinstance(value, ChemicalCompound):
            raise ValueError(f"Field 'hasSolvent' must be an instance of 'ChemicalCompound' or its subclass.")
        return value
    
    @validator("hasSolute", pre=True, always=True)
    def validate_hasSolute(cls, value):
        if value is not None and not isinstance(value, ChemicalCompound):
            raise ValueError(f"Field 'hasSolute' must be an instance of 'ChemicalCompound' or its subclass.")
        return value
    
    

    

    